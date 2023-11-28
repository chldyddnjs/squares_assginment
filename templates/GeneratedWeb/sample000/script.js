window.onload = function() {
    var tweetButton = document.getElementById("tweet-button");
    var tweetInput = document.getElementById("tweet-input");
    var tweetFeed = document.getElementById("tweet-feed");

    tweetButton.addEventListener("click", function() {
        var inputValue = tweetInput.value.trim();

        if (inputValue !== "") {
            var newTweet = document.createElement("p");
            newTweet.textContent = inputValue;

            tweetFeed.appendChild(newTweet);

            // Clear the input field after tweeting
            tweetInput.value = "";
        }
    });
};
