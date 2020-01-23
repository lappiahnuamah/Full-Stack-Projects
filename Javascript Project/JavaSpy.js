const names = "Akosua Brempong";
console.log(names[0]);

const fName = prompt("Please You\'re welcome to this platform. Enter your first name please?");
const lName = prompt("Enter your Last Name please?");
const age = prompt(`How Old are you ${fName} ${lName}`);
const height = prompt("Enter your height in centimeters");
const pet = prompt("Enter your  Name of your pet?");
alert('Thank you for answering the questions');

const age1 = (age > 20 )&& (age < 30) 
const pet1 = pet[pet.length -1];

if((fName[0].toLowerCase()===lName[0].toLowerCase()) && age1 && (height>=175) &&(pet1.toLowerCase() === 'y')) {
    console.log(`Welcome Comrade!, You've passed the Spy Test`);
}else {
    console.log('Sorry nothing to see here');
}
