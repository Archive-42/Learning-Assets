// ==== Objects ====

/* 
  Given the following information about dinosaurs, create 3 objects: 
  Use this pattern to create your objects: 
  object name, diet, weight, length, period
*/

// tyrannosaurus, carnivorous, 7000kg, 12m, Late Cretaceious

const tyrannosaurus = {
  name: 'tyrannosaurus',
  diet: 'carnivorous',
  weight: '7000kg',
  length: '12m',
  period: 'Late Cretaceious',
  roar(){
    return `RAWERSRARARWERSARARARRRR!`;
  }
};

// stegosaurus, herbivorous, 2000kg, 9m, Late Jurassic

const stegosaurus = {
  name: 'stegosaurus',
  diet: 'herbivorous',
  weight: '2000kg',
  length: '9m',
  period: 'Late Jurassic',
};

// velociraptor, carnivorous, 15kg, 1.8m, Late Cretaceious

const velociraptor = {
  name: 'velociraptor',
  diet: 'carnivorous',
  weight: '15kg',
  length: '1.8m',
  period: 'Late Cretaceious',
};

// Using your dinosaur objects, log answers to these questions:

// How much did tyrannosaurus weigh?
console.log(tyrannosaurus.weight);
// What was the diet of a velociraptor?
console.log(velociraptor.diet);
// How long was a stegosaurus?
console.log(stegosaurus.length);
// What time period did tyrannosaurus live in?
console.log(tyrannosaurus.period);

// Create a new roar method for the tyrannosaurus.  When called, return "RAWERSRARARWERSARARARRRR!" Log the result.
console.log(tyrannosaurus.roar());


// ==== Arrays ====

// Given an array of college graduates.  Complete the following requests without using any array methods like .forEach(), .map(), .reduce(), .filter()

const graduates = [{"id":1,"first_name":"Cynde","university":"Missouri Southern State College","email":"ctorry0@macromedia.com"},
{"id":2,"first_name":"Saundra","university":"The School of the Art Institute of Chicago","email":"swhal1@state.gov"},
{"id":3,"first_name":"Lambert","university":"Marian College","email":"lparham2@techcrunch.com"},
{"id":4,"first_name":"Modestine","university":"International Medical & Technological University","email":"mdolder3@symantec.com"},
{"id":5,"first_name":"Chick","university":"Sultan Salahuddin Abdul Aziz Shah Polytechnic","email":"camorts4@google.com.au"},
{"id":6,"first_name":"Jakob","university":"Fachhochschule Rosenheim, Hochschule für Technik und Wirtschaft","email":"jharken5@spiegel.de"},
{"id":7,"first_name":"Robbi","university":"Salem University","email":"rbrister6@redcross.org"},
{"id":8,"first_name":"Colline","university":"Coastal Carolina University","email":"cbrosh7@alibaba.com"},
{"id":9,"first_name":"Michail","university":"Universidad Católica de Ávila","email":"mrome8@shinystat.com"},
{"id":10,"first_name":"Hube","university":"Universitat Rovira I Virgili Tarragona","email":"hlethbrig9@foxnews.com"}]

/* Request 1: Create a new array called universities that contains all the univeristies in the graduates array.  

Once you have the new array created, sort the universities alphabetically and log the result. */
const allUniversities = [];

const getUnis= (arr)=> {for (let i=0; i<arr.length;i++) {
  allUniversities.push(arr[i].university);
  }
}
getUnis(graduates);
console.log(allUniversities);

const universities = [];

const alphabetizeUnis = (arr)=>{
  universities.push(arr.sort());
}

alphabetizeUnis(allUniversities);

console.log(universities)

//**Stretch - sort without the sort method

function sortWithoutSort(arr){
  var minIndex, temporary, length = arr.length;

  for (i=0; i<length; i++){
    minIndex = i;
    for (j=i+1; j<length; j++){
      if(arr[j]<arr[minIndex]){
        minIndex = j;
      }
    }
    temporary = arr[i];
    arr[i] = arr[minIndex];
    arr[minIndex] = temporary;
  }
  return arr;
}

console.log(sortWithoutSort(allUniversities));

//*** Sprint Review: Would like to go over how to create a sort function that calls in the character code (charCodeAt) to give numerical value to the strings we're sorting in this function
// I tried to console.log() through the function but can't figure out where to add charCodeAt to visibly compare the code values

// function sortWithoutSort(arr){
//   var minIndex, temporary, length = arr.length;

//   for (i=0; i<length; i++){
//     minIndex = i; console.log(`First ${minIndex}`);
//     for (j=i+1; j<length; j++){
//       if(arr[j]<arr[minIndex]){
//         minIndex = j;
//         console.log(`Now ${arr[j]}`);console.log(`Next ${arr[j]}`)
//       }
//     }
//     temporary = arr[i]; console.log(`This is temporary ${temporary}`);
//     arr[i] = arr[minIndex]; console.log(`This is arr[i]: ${arr[i]}`);
//     arr[minIndex] = temporary; console.log(`This is arr[minIndex]: ${minIndex}`);
//   }
//   return arr;
// }

/* Request 2: Create a new array called contactInfo that contains both first name and email of each student. 

The resulting contact information should have a space between the first name and the email information like this: 
Name email@example.com

Log the result of your new array. */
const contactInfo = [];

const getInfo = (arr) => {
  for (let i=0; i<arr.length; i++) {
    contactInfo.push(`${arr[i].first_name} ${arr[i].email}`)
  }
}

getInfo(graduates);

console.log(contactInfo);


/* Request 3: Find out how many universities have the string "Uni" included in their name. Create a new array called uni that contains them all. Log the result. */
const uni = [];

const findUni = (arr) => {
  const stringGrads = [];
  for (let i=0; i<arr.length; i++) {
    stringGrads.push(arr[i].university.toString())
    }
  for (let i=0; i<stringGrads.length; i++) {
    if (stringGrads[i].includes('Uni') === true) {
      uni.push(stringGrads[i])
    }
  }
  }

findUni(graduates);

console.log(uni);


// ==== Array Methods ====

// Given this zoo data from around the United States, follow the instructions below

zooAnimals = [{"animal_name":"Jackal, asiatic","population":5,"scientific_name":"Canis aureus","state":"Kentucky"},
{"animal_name":"Screamer, southern","population":1,"scientific_name":"Chauna torquata","state":"Alabama"},
{"animal_name":"White spoonbill","population":8,"scientific_name":"Platalea leucordia","state":"Georgia"},
{"animal_name":"White-cheeked pintail","population":1,"scientific_name":"Anas bahamensis","state":"Oregon"},
{"animal_name":"Black-backed jackal","population":2,"scientific_name":"Canis mesomelas","state":"Washington"},
{"animal_name":"Brolga crane","population":9,"scientific_name":"Grus rubicundus","state":"New Mexico"},
{"animal_name":"Common melba finch","population":5,"scientific_name":"Pytilia melba","state":"Pennsylvania"},
{"animal_name":"Pampa gray fox","population":10,"scientific_name":"Pseudalopex gymnocercus","state":"Connecticut"},
{"animal_name":"Hawk-eagle, crowned","population":10,"scientific_name":"Spizaetus coronatus","state":"Florida"},
{"animal_name":"Australian pelican","population":5,"scientific_name":"Pelecanus conspicillatus","state":"West Virginia"}];

// The zoos need a list of all their animal's names converted to lower case.  Create a new array named lowerCase and map over each name to convert them all to lower case.  Log the resut.
const lowerCase = [];

let lower = zooAnimals.map((item) => {
    lowerCase.push(item.animal_name.toLowerCase())
    })

console.log(lowerCase); 

// The zoos need to know their total animal population across the United States.  Add up all the population numbers from all the zoos using the .reduce() method.
const populationTotal = [];

let totalTally = zooAnimals.reduce(population = (accum, total)=>{return accum += total.population}, 0)
populationTotal.push(totalTally)
console.log(populationTotal);