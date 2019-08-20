
// blackjack game by ritesh aryan

let i,j;

//Card variables
let suits= ['Hearts', 'Clubs','Diamonds','Spades'];
let values=['Ace','King','Queen','Jack','Ten',
             'Nine','Eight','Seven','Six','Five',
             'Four','Three','Two'];
// DOM Variables
let textArea= document.getElementById('text-area');
let newgame= document.getElementById('new-game');
let hit= document.getElementById('hit-button');
let stay= document.getElementById('stay');


// Game Variables

let gameStarted=false,
    gameOver=false,
    playerWon=false,
    dealerCards=[],
    playercards=[],
    dealerScore=0,
    playerScore=0,
    deck=[];


hit.style.display='none';
stay.style.display='none';

newgame.addEventListener('click',function(){

  gameStarted=true;
  gameOver=false;
  playerWon=false;

  deck= CreateDeck();
  shuffleDeck(deck);

  dealerCards=[GetnextCard(),GetnextCard()];
  playerCards=[GetnextCard(),GetnextCard()];

  textArea.innerText= 'Game started.....!!';
  newgame.style.display='none';
  hit.style.display='inline';
  stay.style.display='inline';
  showStatus();


});

hit.addEventListener('click',function(){
  playerCards.push(GetnextCard());
  checkForEndOfGame();
  showStatus();
});

stay.addEventListener('click',function(){
  gameOver=true;
  checkForEndOfGame();
  showStatus();
});

function CreateDeck(){
  let deck=[];
  for( i=0;i<suits.length;i++){
  for(j=0;j<values.length;j++){
    let card={
      suit:suits[i],
      value:values[j]
      };
    deck.push( card );
  }
}
return deck ;
}


/* for(i=0;i<deck.length;i++){
  console.log(deck[i]);
} */

function GetnextCard(){
  return deck.shift();
}

function shuffleDeck(deck){
  let i,j,temp;
  for(i=0;i<deck.length;i++){
    j=Math.trunc(Math.random()*deck.length);
    temp=deck[j];
    deck[j]=deck[i];
    deck[i]=temp;

  }
}

function GetCardString(card){
  return card.value+"  of "+card.suit;
}

function getcardNumericValue(card){
  switch (card.value) {
    case 'Ace':
    return 1;
    case 'Two':
    return 2;
    case 'Three':
    return 3;
    case 'Four':
    return 4;
    case 'Five':
    return 5;
    case 'Six':
    return 6;
    case 'Seven':
    return 7;
    case 'Eight':
    return 8;
    case 'Nine':
    return 9;
    default:
    return 10;

  }
}

function getScore(cardArray){
  let score=0;
  let hasAce=false;
  let i;
  for(i=0;i<cardArray.length;i++){
    let card= cardArray[i];
    score+=getcardNumericValue(card);
    if(card.value==='Ace'){
      hasAce=true;
    }
  }
  if(hasAce && score+10 <=21){
    return score+10;
  }
  return score;
}



function updateScores(){
  dealerScore=getScore(dealerCards);
  playerScore= getScore(playerCards);
}

function checkForEndOfGame(){
  updateScores();
  if(gameOver){
    //let the dealer take cards
    while(dealerScore<playerScore && playerScore<= 21 && dealerScore<= 21  ){
      dealerCards.push(GetnextCard());
      updateScores();
    }
  }

  if(playerScore >21){
    playerWon=false;
    gameOver=true;
  }
  else if(dealerScore>21){
    playerWon=true;
    gameOver=true;
  }

  else if(gameOver){
    if(playerScore > dealerScore){
      playerWon=true;
    }
    else {
      playerWon=false;
    }


  }
}

function showStatus(){
  if(!gameStarted)
  {
    textArea.innerText='Welcome to Black Jack ..!!';
  }

  for(let i=0;i<deck.length;i++){
    textArea.innerText+='\n'+GetCardString(deck[i]);
  }

  let dealerCardString='';
  for(let i=0;i<dealerCards.length;i++){
    dealerCardString+=GetCardString(dealerCards[i])+'\n';
  }

  let playerCardString='';
  for(let i=0;i<playerCards.length;i++){
    playerCardString+=GetCardString(playerCards[i])+'\n';
  }

  updateScores();
  textArea.innerText= 'Dealer has\n '+
                      dealerCardString +
                      '( score: ' +dealerScore +')\n\n'+

                      'Player has \n '+
                      playerCardString +
                      '( score: '+ playerScore +') \n\n';

  if(gameOver){
    if(playerWon){
      textArea.innerText+='You Win';
    }
    else{
      textArea.innerText+='Dealer Wins';
    }
    newgame.style.display='inline';
    hit.style.display='none';
    stay.style.display='none';
  }
}
console.log("Welcome to Black Jack Game");
console.log("You are Dealt: ");
//console.log(" "+ GetCardString(play[0]));
//console.log(" "+GetCardString(play[1]));
