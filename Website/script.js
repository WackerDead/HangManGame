var isRunning = false;
var theme = "";
var word = "";
var fails = 0;
var hiddenWord = "";
var lettersNotInWord = "";

function Init () {
    isRunning = true;
    word = document.getElementById( "InputBoxWord" ).value;
    theme = document.getElementById( "InputBoxTheme" ).value;
    fails = 0;
    for ( let i = 0; i < word.length; i++ ) {
        hiddenWord += ( word[i] == " " ) ? " " : "_"
    }
    //StartGame();
    UpdateUI();
}

function StartGame () {

}

function WriteLetters () {

    /*if ( WinOrLose() ) {
        return;
    }*/
    //WinOrLose();

    let input = document.getElementById( "Input" ).value.toLowerCase();
    console.log( input );
    let lowerWord = word.toLowerCase();

    if ( lowerWord.includes( input ) ) {
        for ( const letter of input ) {
            for ( let i = 0; i < lowerWord.length; i++ ) {
                if ( lowerWord[i] == letter ) {
                    hiddenWord = hiddenWord.substring( 0, i ) + word[i] + hiddenWord.substring( i + 1 );
                }
            }
        }
    }
    else if ( !lettersNotInWord.includes( input ) ) {
        lettersNotInWord += input + ",";
        fails++;
    }

    UpdateUI();
}

function UpdateUI () {
    document.getElementById( "HiddenWord" ).innerText = hiddenWord;
    document.getElementById( "LetterNotInWord" ).innerText = lettersNotInWord;

    document.getElementById( "Input" ).value = "";
}

function WinOrLose () {
    if ( hiddenWord == word ) {
        console.log( "You Won" );
        return true;
    }
    else if ( fails >= 6 ) {
        console.log( "You Lost" );
        return true;
    }
    return false;
}