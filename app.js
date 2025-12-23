const languageMap = {  // Fixed typo: langaugeMap -> languageMap
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Chinese': 'zh-cn',
    'Yoruba': 'yo',  // Fixed capitalization
    'Krio': 'kri'
}

let selectedLanguage = 'en';  // Fixed typo: selectedLangauge -> selectedLanguage
let videoLoaded = false;

//translation button
document.getElementById("load_video_btn").onclick = async function () {  // Fixed typo: conclick -> onclick
    const button = this;
    const urlInput = document.getElementById("user_website_enter_form").value;  // Added .value
    
    //to check if it has a valid url input
    //Error handling
    if (!urlInput.includes("youtube.com") && !urlInput.includes("youtu.be")) {  // Fixed typo: include -> includes
        alert("Please enter a valid YouTube URL.");
        return;
    }
    
    if (!videoLoaded) {  // check if vid is loaded
        let embedUrl = urlInput;
        if (urlInput.includes("watch?v=")) {  // Added if statement
            embedUrl = urlInput.replace("watch?v=", "embed/");  // Fixed: replaceChild -> replace
        } else if (urlInput.includes("youtu.be/")) {
            embedUrl = "https://www.youtube.com/embed/" + urlInput.split("youtu.be/")[1];
        }
        document.getElementById("youtube_iframe").src = embedUrl;  
        button.innerHTML = "Translate Video";
        videoLoaded = true;  
        return;  // Added return to exit after loading video
    }

    // Translation code (runs on second click)
    button.innerHTML = "Translating...";
    button.disabled = true;

    try {
        const response = await fetch("http://127.0.0.1:5000/translate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                url: urlInput,
                language: selectedLanguage  // Fixed: = -> : and selectedLangauge -> selectedLanguage
            }),
        });
        
        if (response.ok) {
            const blob = await response.blob();
            //Download url
            const downloadUrl = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = downloadUrl;
            a.download = 'translated_audio.mp3';
            document.body.appendChild(a);  // Added this line - important!
            a.click();
            a.remove();
            
            alert("Translation Complete. Audio file downloaded");
        } else {
            const error = await response.json();
            alert("Error: " + (error.Error || error.error || "Translation failed"));
        }
    } catch (err) {
        alert("Translation failed: " + err.message);
    }

    button.innerHTML = "Translate Video";
    button.disabled = false;
};

// Language dropdown handler
function show_language(event) {
    event.preventDefault();
    const languageName = event.target.textContent;
    // Set the dropdown button text to the selected language
    document.getElementById('dropdownMenuButton1').textContent = languageName;
    // Store the language code
    selectedLanguage = languageMap[languageName] || 'es';
}