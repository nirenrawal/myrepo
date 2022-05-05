function _one(q, e=document){return e.querySelector(q)}
function _all(q, e=document){return e.querySelectorAll(q)}

// const tweetPostElement = document.querySelector('#tweet-post');
const addTweetForm = document.querySelector('.creatTweet');
// const btnSubmit = document.querySelector('#submit-main-tweet');
const tweetInput = document.querySelector('#tweet-input');
const tweetText = document.querySelectorAll('.tweetText');
const editSubmitButton = document.querySelector('#update-submit-btn');


/////////////////////////////// TWEET OVERLAY //////////////////////////////////////
function toggleCreateTweetModal(){
    document.querySelector("#createTweetModal").classList.toggle("hidden")
}
function toggleUpdateTweetModal(){
    document.querySelector("#updateTweetModal").classList.toggle("hidden")
}
function openEditForm(tweet_id) {
    let tweetText = document.querySelector(`[id='${tweet_id}']`).children[0].children[1].childNodes[5]
    tweetInput.value = tweetText.innerText
    editSubmitButton.setAttribute('onclick', `edit('${tweet_id}')`)
    
    toggleUpdateTweetModal()
}

/////////// CREATE TWEET - FETCH //////////////
async function createTweet(){
    const form = event.target
    // Get the button, set the data-await, and disable it
    const button = _one("button[type='submit']", form)
    button.innerText = button.dataset.await
    // button.innerText = button.getAttribute("data-await")
    button.disabled = true
  
    user_id = document.querySelector(".login-user-id").id
  
    const connection = await fetch(`/tweets-create/${user_id}`, {
      method : "POST",
      body : new FormData(form)
    })
  
    button.disabled = false
    button.innerText = button.dataset.default
  
    if( ! connection.ok ){
      return
    }
    const res = await connection.json();
    const tweet = res.tweet
    
    let tweet_post = `
      <div id="${tweet.tweet_id}" class="p-4 border-t border-slate-200">
        <div class="flex">
          <img class="flex-none w-12 h-12 object-cover rounded-full userProfile" src="/images/${tweet.user_image}">
          
          <div class="w-full pl-4">
            <!-- first name - username/ text -->
            <span onclick="goToUserProfile('${tweet.user_id}')" class="cursor-pointer">
              <div id="user-info" class="flex">
                  <p class="font-bold pr-2">
                    ${tweet.user_first_name} ${tweet.user_last_name}
                  </p>
                  <p class="font-thin">
                    @${tweet.user_name} - <span class="ml-1 text-xs font-light">${tweet['tweet_created_at']}</span>
                  </p>                        
              </div>
            </span>
           
            <div id="tweet-text" class="pt-2 test07">
              ${tweet.tweet_text}
            </div>

            
         



          

            <div class="flex flex-row mt-4 text-lg text-gray-400 ">
                    <div class="hover:text-blue1 basis-2/12">
                <i onclick="openEditForm(${tweet['tweet_id']})" id="edit-tweet"
                  class="editBtn fa-solid fa-pen cursor-pointer"></i>
              </div>

              <div class="hover:text-red-700 basis-2/12">
                <i onclick="deleteTweet(${tweet['tweet_id']})" class="fas fa-trash ml-auto cursor-pointer"></i>
              </div>

              <div class="hover:text-green-700 cursor-pointer basis-2/12">
                <i class="fa-solid fa-message ml-auto"></i>
              </div>

              <div class="hover:text-pink-600 flex-auto basis-2/12">
                <button type="button" onclick="likeTweet(${tweet['tweet_id']})">
                  <i class="fa-solid fa-heart"></i>
                </button> <span class="text-sm" id="likes{{tweet['tweet_id']}}" value="0"></span>
              </div>
              <div class="hover:text-blue1 basis-2/12">
                <i class="fa-solid fa-retweet"></i>
              </div>
              <div class="hover:text-blue1 basis-2/12">
                <i class="fa-solid fa-share-nodes"></i>
              </div>

            
          </div>
        </div>
      </div>
      `
    incrementedValueMainElement.innerText = 0
    incrementedValueQuickElement.innerText = 0
    document.querySelector(".tweet-post").insertAdjacentHTML("afterbegin", tweet_post)
    _one(".createTweet", form).value = ""
    document.querySelector("#createTweetModal").classList.add("hidden")
   
    hideBrokenImage();
}

function likeTweet(tweet_id) {
  const element = document.getElementById("likes" + tweet_id);
  value = parseInt(element.getAttribute("value"), 10) + 1;
  element.setAttribute("value", value)
  element.innerHTML = value;

}

// UPDATE TWEET //
async function updateTweet(tweet_id) {
    let tweetText = document.querySelector(`[id='${tweet_id}']`).children[0].children[1].childNodes[5]
    document.querySelector(`[id='${tweet_id}']`).children[0].children[1].children[2].childNodes[0]
    let image = document.querySelector(`[id='${tweet_id}']`).children[0].children[1].children[2]
    console.log(image);
  
    const form = event.target.form
    toggleUpdateTweetModal()
    const connection = await fetch(`/tweets/${tweet_id}`, {
        method: "PUT",
        body: new FormData(form)
    })
    if (!connection.ok) {
        alert("Could not connect")
        return
    }
    let editedTweet = await connection.json()
    let tweet_text = editedTweet.tweet.tweet_text
    let tweet_image = editedTweet.tweet.tweet_image
    tweetText.innerText = tweet_text
    
    img = `<img onerror="this.style.display='none'" class="mt-2 w-full object-cover h-80 rounded-2xl tweet-image" src="/static/images/user_content_images/${tweet_image}">`

    image.innerHTML = img
    
    document.querySelector(".editTweet-image-update").value = ""
    
}

/////////// DELETE TWEET //////////////
async function deleteTweet(tweet_id) {
    const connection = await fetch(`/tweets/${tweet_id}`, {
        method : "DELETE"
    })
    if (!connection.ok) {
        alert("uppps... try again")
        return
    }
    document.querySelector(`[id='${tweet_id}']`).remove()
}






const creteTweetInputElement = document.querySelector(".create-tweet-input");
const incrementedValueMainElement = document.querySelector(".remaining-chars-main");

const quickTweetInputElement = document.querySelector(".quick-tweet-input")
const incrementedValueQuickElement = document.querySelector(".incremented-chars-quick")


function updateCharactersMain() {
  const enteredText = event.target.value;
  const enteredTextLength = enteredText.length;
  const outputTextLength =  + enteredTextLength;
  incrementedValueMainElement.textContent = outputTextLength;
}

function updateCharactersQuick() {
  const enteredText = event.target.value;
  const enteredTextLength = enteredText.length;
  const outputTextLength =  + enteredTextLength;
  incrementedValueQuickElement.textContent = outputTextLength;
}


// //////////////////////////////////////////////////////////////////////  JQuery  //////////////////////////////////////////////////////////////////////////////////////
// JQuery - hide borken image //
function hideBrokenImage() {
    $('.userProfile').on("error", function() {
        $(this).attr('src', '/static/images/user_profile_pictures/default_profile_picture.png');
    });

    // Hide broken img when img not passed
    $(".tweetImg").on("error", function() {
        $(this).hide();
    });
}

// Get image file_name
const file = document.querySelector(".editTweet");
function getFileName(){ 
document.querySelector(".display-filename").innerText = file.value.split('\\').pop().split('/').pop();
};