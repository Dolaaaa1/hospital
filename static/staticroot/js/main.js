// setting up firebase with our website
const firebaseApp = firebase.initializeApp({
    apiKey: "AIzaSyDgVvLohk_hLuYXAwMpdh8vJKM-MPMv4vI",
  authDomain: "nasrooo.firebaseapp.com",
  databaseURL: "https://nasrooo-default-rtdb.firebaseio.com",
  projectId: "nasrooo",
  storageBucket: "nasrooo.appspot.com",
  messagingSenderId: "606558294259",
  appId: "1:606558294259:web:b146024d80777b6432a786",
  measurementId: "G-MD3PRVZ4K5"
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
            console.log(error.code);
            console.log(error.message)
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
            console.log(error.code);
            console.log(error.message)
        });
}