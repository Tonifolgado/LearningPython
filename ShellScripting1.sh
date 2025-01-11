
#!/bin/sh
username= "Sam" #Variables
filename=$1

read -p "Enter your age: " age  #User Input
echo "Your age is: $age"

if ["SUID" -ne 0]; then #Conditional Statements
echo "You are not a root user."
else
echo "You are running this script as root."
fi

echo "Looping through numbers:" #For Loop
for i in 12 3 4 5
do
  echo "Number: $i"
done

hello() {
  echo "Hello, $1!"
}
hello "World"

echo "Select an option: 1 or 2"   #Conditional Case Statements
read choice 
case $choice in
1) echo "Option 1 selected." :
2) echo "Option 2 selected." :
*) echo "Invalid selection." 
esac

if [-e "$filename" ); then    #File Operations
 echo "The file exists." 
else
 echo "File not found."
fi

echo "First argument: $1"  #Command Line Arguments
echo "Second argument: $2"

touch temp.txt && rm temp.txt 2>/dev/null  #Exit Status Codes
echo "Exit code: $?"

fruits=("Apple" "Grape" "Peach") #Indexed Arrays
echo "First fruit: ${fruits[O]}"

declare -A countries  #Associative Arrays
countries[UK]="London" 
countries [Japan]="Tokyo"
echo "Capital of UK: $(countries(UK])"

today=$(date)  #Command Substitution
echo "Today's date: Stoday"

echo "Sample Output"> instead adding
