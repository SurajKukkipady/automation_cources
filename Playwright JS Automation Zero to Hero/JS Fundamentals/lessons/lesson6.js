// Conditional Statements

if (true) {
  console.log("This will always run");
} else {
  console.log("This will never run");
}

// If hours between 6 and 12, print "Good morning"
// If hours between 12 and 18, print "Good afternoon"
// Else print "Good evening"

var hours = 10;

if (hours >= 6 && hours < 12) {
    console.log("Good morning");
} else if (hours >= 12 && hours < 18) {
    console.log("Good afternoon");
} else {
    console.log("Good evening");
}