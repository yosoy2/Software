#define I2C_Address 0x10
#define SCL_PORT PORTC
#define SDA_PORT PORTC
#define SCL_PIN 5
#define SDA_PIN 4
#define pin_servo_lidar 9

#define reinicio 500

#include <ros.h>
#include <duckietown_msgs/lidar_9.h>
#include <I2C.h>
#include <Servo.h>


#define angulo_inicial 0
#define angulo_final 180
#define angulo_paso 10
#define tiempo_espera 20

ros::NodeHandle nh ;

duckietown_msgs::lidar_9 str_msg ;
ros::Publisher lidarTopic("lidarTopic",&str_msg) ;

Servo servo_lidar;

uint8_t i, m;
int j;
int angulo = 0;
int inicio = 0;
int x;

void setup() {

    
    servo_lidar.attach(pin_servo_lidar);
  
    I2c.begin(); 
    I2c.setSpeed(0);  //0 is the 100KHz 1 is 400KHz
    I2c.pullup(0);    //disable internal pullup resistors
    I2c.timeOut(35);  //after 35ms I2C will release itself and re-initialize 

    nh.initNode();
    nh.advertise(lidarTopic);

    Serial.begin(57600); // start serial communication at 57600bps


}

void loop() {

  if(inicio==0){
  Serial.println(F(": tinyLiDAR preset to High Speed configuration.  \n\r"));
  writeCommand(I2C_Address,"PS"); 
  delay(reinicio);
  inicio = 1;}
  
  for (angulo = angulo_inicial; angulo <= angulo_final-angulo_paso; angulo += angulo_paso) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    servo_lidar.write(angulo);              // tell servo to go to position in variable 'pos'
    x=Distancia(1, 0, I2C_Address);    
    str_msg.angulo = angulo;
    str_msg.distancia =x;    
    lidarTopic.publish(&str_msg);
    Serial.print(F("     Angulo = "));
    Serial.println(angulo);     // print the Measured_Distance if not 0
    delay(tiempo_espera);                       // waits 15ms for the servo to reach the position
  }

  for (angulo = angulo_final; angulo >= angulo_inicial+angulo_paso; angulo -= angulo_paso) { // goes from 180 degrees to 0 degrees
    servo_lidar.write(angulo);              // tell servo to go to position in variable 'pos'
    x=Distancia(1, 0, I2C_Address);
    str_msg.angulo = angulo;
    str_msg.distancia =x;    
    lidarTopic.publish(&str_msg);
    Serial.print(F("     Angulo = "));
    Serial.println(angulo);     // print the Measured_Distance if not 0
    delay(tiempo_espera);                       // waits 15ms for the servo to reach the position
  }
  
    nh.spinOnce();
    delay(tiempo_espera);

}

int Distancia(byte j, byte delayBetween, uint8_t targetAddr)  // j num of bytes, up to 255ms delay between and from targetAddr
{

    for (byte i =0;i<j;i++)
    {
        int Measured_Distance = Read_Distance(targetAddr); 

        if (Measured_Distance) {

            Serial.print(F("     Distancia = "));
            Serial.print(Measured_Distance);     // print the Measured_Distance if not 0
            Serial.println(F("mm"));
            return Measured_Distance;

        } else 
        {
            
            Serial.println(F("     Distancia = Invalida"));           //invalid distance data will show as '-'

        } // if else

        delay(delayBetween); 

    } //for i
}
    
uint16_t Read_Distance(uint8_t targetAddr) 
{

    uint16_t i;
    if( !I2c.write(targetAddr,'D') ) 
    {     

        i = I2c.read(targetAddr,2); //request 2 bytes for distance

        while ( I2c.available() ) 
        { 

            i = I2c.receive();        // receive 1st byte
            i = i<<8 | I2c.receive(); // receive 2nd byte

        } 

    }
    else
    {

        Serial.print(F(" Error talking to device at address 0x")); 
        Serial.println(targetAddr, HEX);
        return 0; //exit

    } //if else
    
    return i;

} //Read_Distance()

void writeCommand(uint8_t targetAddr, String command)
{

    if (command.length() == 2)
    {

         I2c.write(targetAddr,command.charAt(0), command.charAt(1)); 

    }else{

        I2c.write(targetAddr,command.charAt(0) ); 

    } // if else

}
