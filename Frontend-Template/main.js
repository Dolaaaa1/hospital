// setting up firebase with our website
const firebaseApp = firebase.initializeApp({
  apiKey: "AIzaSyCcEbP6UX4xalyq8hsZ14bCzIg7cziysNA",
  authDomain: "ahmed-5f07c.firebaseapp.com",
  projectId: "ahmed-5f07c",
  storageBucket: "ahmed-5f07c.appspot.com",
  messagingSenderId: "981024707554",
  appId: "1:981024707554:web:235c9af2f048846d50dfbb",
  measurementId: "G-4M1EFM4Z94"
});
const db = firebaseApp.firestore();
const auth = firebaseApp.auth();

// Sign up function
const signUp = () => {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    console.log(email, password)
    // firebase code
    firebase.auth().createUserWithEmailAndPassword(email, password)
        .then((result) => {
            // Signed in 
            document.write("You are Signed Up")
            console.log(result)
            // ...
        })
        .catch((error) => {
            alert(error.code);
            alert(error.message)
            // ..
        });
}

// Sign In function
const signIn = () => {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    // firebase code
    firebase.auth().signInWithEmailAndPassword(email, password)
        .then((result) => {
            // Signed in 
            document.write("You are Signed In")
            console.log(result)
        })
        .catch((error) => {
            alert(error.code);
            alert(error.message)
        });
}