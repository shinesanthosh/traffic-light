#include <LiquidCrystal.h>

LiquidCrystal lcd(7, 6, 5, 4, 3, 2);


void setup() 
{
	
  Serial.begin(9600);
  
  for (int thisPin = 2; thisPin <= 13; thisPin++) {
    pinMode(thisPin, OUTPUT);
  }

  lcd.begin(16,2);
  lcd.clear();
  lcd.setCursor(1,0);
  lcd.print("Arduino Home");
  lcd.setCursor(2,1);
  lcd.print("Automation");
  delay(1000);
  lcd.clear();
  }

String command;

void loop() 
{
	
	
  checkSerial();
  
}


void checkSerial(){
  
  char c = Serial.read();
  
  if(c != -1)
  {
    if(c=='=')
    {
      Serial.print('\n');
      divrem(command);
      command="";
      }
    else
      {
        command += c;
        Serial.print(c);
        }
    }
  
  }

int divrem(String com)
{
  String part1 = com.substring(0,com.indexOf(" "));
  String part2 = com.substring(com.indexOf(" ")+1);
  int pin = part2.toInt();
  
  if(part1.equalsIgnoreCase("pinon")){
	  digitalWrite(pin,HIGH);
    //Serial.print('1');
    }
 else if(part1.equalsIgnoreCase("pinoff")){
    digitalWrite(pin,LOW);
    //Serial.print('1');
    }
 else if(part1.equalsIgnoreCase("bright"))
    {
     analogWrite(11,pin);
    }
    else if(part1.equalsIgnoreCase("lcd"))
    {
    lcd.print(part2);
    //Serial.print('1');
    }
    else if(part1.equalsIgnoreCase("lcdclear"))
    {
        lcd.clear();
      }
    }


  
