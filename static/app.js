class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
            voiceButton: document.querySelector('.click_to_convert'),
            dropdowns: document.querySelectorAll('.dropdown'),
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const { openButton, chatBox, sendButton, voiceButton, dropdowns } = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        voiceButton.addEventListener('click', () => this.onVoiceButton(chatBox))

        dropdowns.forEach(dropdown => {
            const select = dropdown.querySelector('.select');
            const caret = dropdown.querySelector('.caret');
            const menu = dropdown.querySelector('.menu');
            const options = dropdown.querySelectorAll('.menu li');
            const selected = dropdown.querySelectorAll('.selected');

            select.addEventListener('click', () => {
                select.classList.toggle('select-clicked');
                caret.classList.toggle('caret-rotate');
                menu.classList.toggle('menu-open');
            });

            options.forEach(option => {
                option.addEventListener('click', () => {
                    selected.innerText = option.innerText;
                    select.classList.remove('select-clicked');
                    caret.classList.remove('caret-rotate');
                    menu.classList.remove('menu-open');

                    options.forEach(option => {
                        option.classList.remove('active');
                    });

                    option.classList.add('active');
                });
            });
        });
        chatBox.classList.add('chatbox--active')
        this.onStart(chatBox);

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({ key }) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // show or hides the box
        if (this.state) {
            chatbox.classList.remove('chatbox--hide')
            chatbox.classList.add('chatbox--active')
            this.onStart(chatbox);
        } else {
            chatbox.classList.remove('chatbox--active')
            chatbox.classList.add('chatbox--hide')
        }
    }

    async onVoiceButton(chatbox) {
        const etat = document.querySelector('.active').innerText;
        let Langue
        let Langue2
        switch (etat) {
            case 'Français':
                Langue = "fr-FR";
                Langue2 = "fr";
                this.sendChatText(chatbox, "Fonctionnalité vocale encours. Vous pouvez parler.");
                break;
            case 'English':
                Langue = "en-EN";
                Langue2 = "en";
                this.sendChatText(chatbox, "Outstanding voice functionality. You can talk.");
                break;
            case 'Español':
                Langue = "es-Es";
                Langue2 = "es";
                this.sendChatText(chatbox, "Excelente funcionalidad de voz. Puedes hablar.");
                break;
            case 'Deutsch':
                Langue = "de-AT";
                Langue2 = "de";
                this.sendChatText(chatbox, "Hervorragende Sprachfunktion. Du kannst reden.");
                break;
            case 'Chinese':
                Langue = "zh-CN";
                Langue2 = "zh";
                this.sendChatText(chatbox, "出色的语音功能。你可以说了。");
                break;
            case 'Hausa':
                Langue = "Non";
                Langue2 = "Non";
                this.sendChatText(chatbox, "Har yanzu babu aikin murya.");
                break;
            case 'Igbo':
                Langue = "Non";
                Langue2 = "Non";
                this.sendChatText(chatbox, "Ọrụ olu adịbeghị.");
                break;
            case 'Yoruba':
                Langue = "Non";
                Langue2 = "Non";
                this.sendChatText(chatbox, "Išẹ ohun ko si sibẹsibẹ wa.");
                break;
            case 'Arabic':
                Langue = "ar-AE";
                Langue2 = "ar";
                this.sendChatText(chatbox, "وظائف صوتية رائعة. تستطيع التحدث.");
                break;
            case 'Zulu':
                Langue = "zu-ZA";
                Langue2 = "zu";
                this.sendChatText(chatbox, "Ukusebenza kwezwi okuvelele. Ungakhuluma.");
                break;
            case 'Russian':
                Langue = "ru-RU";
                Langue2 = "ru";
                this.sendChatText(chatbox, "Выдающаяся голосовая функциональность. Ты можешь говорить.");
                break;
            case 'Nyanja':
                Langue = "Non";
                Langue2 = "Non";
                this.sendChatText(chatbox, "Kugwira ntchito kwa mawu sikunapezeke");
                break;
            case 'Italiano':
                Langue = "it-IT";
                Langue2 = "it";
                this.sendChatText(chatbox, "Eccezionale funzionalità vocale. Puoi parlare.");
                break;
            case 'Creole':
                Langue = "Non"
                Langue2 = "Non";
                this.sendChatText(chatbox, "Fonksyonalite vwa poko disponib.");
                break;
            case 'Hébreux':
                Langue = "he-IL";
                Langue2 = "he";
                this.sendChatText(chatbox, "פונקציונליות קול יוצאת דופן. אתה יכול לדבר.");
                break;
            case 'Japonais':
                Langue = "ja-JP";
                Langue2 = "ja";
                this.sendChatText(chatbox, "優れた音声機能。あなたは話すことができます。");
                break;
            case 'Malagasy':
                Langue = "Non"
                Langue2 = "Non";
                this.sendChatText(chatbox, "Mbola tsy misy ny fampiasa feo.");
                break;
            case 'Soomaali':
                Langue = "so-SO";
                Langue2 = "so";
                this.sendChatText(chatbox, "Shaqaynta codka aadka u wanaagsan. Waad hadli kartaa.");
                break;
            case 'Kiswahili':
                Langue = "sw-KE";
                Langue2 = "sw";
                this.sendChatText(chatbox, "Utendaji bora wa sauti. Unaweza kuzungumza.");
                break;
            case 'Amharic':
                Langue = "am-ET";
                Langue2 = "am";
                this.sendChatText(chatbox, "የላቀ የድምፅ ተግባር። ማውራት ትችላለህ።");
                break;
            case 'Hindi':
                Langue = "hi-IN";
                Langue2 = "hi";
                this.sendChatText(chatbox, "उत्कृष्ट आवाज कार्यक्षमता। तुम बात कर सकते हो।");
                break;
            case 'Portuguese':
                Langue = "pt-PT";
                Langue2 = "pt";
                this.sendChatText(chatbox, "Excelente funcionalidade de voz. Você pode falar.");
                break;
            default:
                Langue = "fr-FR";
                Langue2 = "fr";
                this.sendChatText(chatbox, "Fonctionnalité vocale encours. Vous pouvez parler.");
                break;
        }

        function Speech(chatbox, langue) {
            if ('webkitSpeechRecognition' in window) {
                // creating voice capture object
                var textField = chatbox.querySelector('input');
                this.recognition = new webkitSpeechRecognition();

                // settings
                this.recognition.continuous = true; // not stop automatically
                this.recognition.interimResults = false;
                this.recognition.lang = langue

                this.startCapture = function() {
                    this.recognition.start();
                }

                this.stopCapture = function() {
                    this.recognition.stop();
                }

                this.recognition.onresult = function(event) {
                    textField.value = event.results[0][0].transcript;
                }

                this.recognition.onerror = function(event) {
                    console.log(event.error);
                }
                console.log("webkitSpeechRecognition is available.");
            } else {
                console.log("webkitSpeechRecognition is not available.");
                textField.value = "Navigateur non supporté"
            }
        }

        let text1 = ''
        var textField = chatbox.querySelector('input');

        if (Langue != "Non") {
            var speech = new Speech(chatbox, Langue);
            speechSynthesis.cancel();
            speech.startCapture();
            textField.disabled = true;
        }

        function testAsync(speech) {
            return new Promise((resolve, reject) => {
                //here our function should be implemented
                setTimeout(() => {
                    console.log("Hello from inside the testAsync function 2");
                    speech.stopCapture();
                    setTimeout(() => {
                        console.log("Hello from inside the testAsync function 1");
                        resolve();
                    }, 4000);
                }, 4500);
            });
        }

        await testAsync(speech);
        text1 = textField.value;
        textField.value = "";
        console.log(text1)

        textField.disabled = false;
        if (text1 === "") {
            text1 = "aucun son";
        }

        switch (etat) {
            case 'Français':
                this.sendChatText(chatbox, "Traitement en cours veuillez patienter⏳. Le temps d'attente dependra de votre connexion internet🌐🧑‍💻.");
                break;
            case 'English':
                this.sendChatText(chatbox, "Treatment in progress please wait⏳. The waiting time will depend on your internet🌐🧑 💻 connection.");
                break;
            case 'Español':
                this.sendChatText(chatbox, "Procesando en progreso por favor espere⏳. El tiempo de espera dependerá de tu conexión a internet🌐🧑‍💻.");
                break;
            case 'Deutsch':
                this.sendChatText(chatbox, "Bearbeitung läuft, bitte warten⏳. Die Wartezeit hängt von Ihrer Internetverbindung ab🌐🧑‍💻.");
                break;
            case 'Chinese':
                this.sendChatText(chatbox, "處理中請稍候⏳。 等待時間取決於您的網絡連接🌐🧑‍💻。");
                break;
            case 'Hausa':
                this.sendChatText(chatbox, "Ana ci gaba da aiwatarwa da fatan za a jira⏳. Lokacin jira zai dogara ne akan haɗin intanet ɗin ku🌐🧑‍💻.");
                break;
            case 'Igbo':
                this.sendChatText(chatbox, "Nhazi na-aga n'ihu, biko chere⏳. Oge nchere ga-adabere na njikọ ịntanetị gị🌐🧑‍💻.");
                break;
            case 'Yoruba':
                this.sendChatText(chatbox, "Ilọsiwaju lọwọ jọwọ duro⏳. Akoko idaduro yoo da lori asopọ intanẹẹti rẹ🌐🧑‍💻.");
                break;
            case 'Arabic':
                this.sendChatText(chatbox, "المعالجة جارية ، يرجى الانتظار⏳. سيعتمد وقت الانتظار على اتصالك بالإنترنت🌐🧑‍💻.");
                break;
            case 'Zulu':
                this.sendChatText(chatbox, "Ukucubungula kuyaqhubeka sicela ulinde⏳. Isikhathi sokulinda sizoncika ekuxhumekeni kwakho kwe-inthanethi🌐🧑‍💻.");
                break;
            case 'Russian':
                this.sendChatText(chatbox, "Идет обработка, пожалуйста, подождите⏳. Время ожидания будет зависеть от вашего интернет-соединения🌐🧑‍💻.");
                break;
            case 'Nyanja':
                this.sendChatText(chatbox, "Kukonza kuli mkati chonde dikirani⏳. Nthawi yodikirira idzatengera intaneti yanu🌐🧑‍💻.");
                break;
            case 'Italiano':
                this.sendChatText(chatbox, "Elaborazione in corso attendere⏳. Il tempo di attesa dipenderà dalla tua connessione internet🌐🧑‍💻.");
                break;
            case 'Creole':
                this.sendChatText(chatbox, "Pwosesis la ap fèt tanpri tann⏳. Tan ap tann lan pral depann de koneksyon entènèt ou🌐🧑‍💻.");
                break;
            case 'Hébreux':
                this.sendChatText(chatbox, "העיבוד מתבצע, אנא המתן⏳. זמן ההמתנה יהיה תלוי בחיבור האינטרנט שלך🌐🧑‍💻.");
                break;
            case 'Japonais':
                this.sendChatText(chatbox, "処理中です。しばらくお待ちください⏳。 待ち時間はインターネット接続状況によって異なります🌐🧑‍💻。");
                break;
            case 'Malagasy':
                this.sendChatText(chatbox, "Eo am-pikarakarana azafady ⏳. Ny fotoana fiandrasana dia hiankina amin'ny fifandraisanao amin'ny Internet🌐🧑‍💻.");
                break;
            case 'Soomaali':
                this.sendChatText(chatbox, "Howsha ayaa socota fadlan sug⏳. Waqtiga sugitaanka wuxuu ku xirnaan doonaa isku xirka interneedkaaga🌐🧑‍💻.");
                break;
            case 'Kiswahili':
                this.sendChatText(chatbox, "Inachakata tafadhali subiri⏳. Muda wa kusubiri utategemea muunganisho wako wa intaneti🌐🧑‍💻.");
                break;
            case 'Amharic':
                this.sendChatText(chatbox, "በሂደት ላይ ነው እባክዎ ይጠብቁ⏳። የጥበቃ ጊዜ በእርስዎ የበይነመረብ ግንኙነት🌐🧑‍💻 ይወሰናል።");
                break;
            case 'Hindi':
                this.sendChatText(chatbox, "प्रसंस्करण प्रगति पर है कृपया प्रतीक्षा करें⏳। प्रतीक्षा समय आपके इंटरनेट कनेक्शन पर निर्भर करेगा।");
                break;
            case 'Portuguese':
                this.sendChatText(chatbox, "Processamento em andamento, aguarde⏳. O tempo de espera dependerá da sua conexão com a internet🌐🧑‍💻.");
                break;
            default:
                this.sendChatText(chatbox, "Traitement en cours veuillez patienter⏳. Le temps d'attente dependra de votre connexion internet🌐🧑‍💻.");
        }

        function textToAudio(langue, message) {
            if ('speechSynthesis' in window) {
                console.log('supported');
                let msg = message
                let speech = new SpeechSynthesisUtterance();
                speech.lang = langue;

                speech.text = msg;
                speech.volume = 1;
                speech.rate = 1;
                speech.pitch = 1;

                speechSynthesis.cancel();
                speechSynthesis.speak(speech);

            } else {
                console.log('not supported');
            }
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        let lien = this.FindRoute()

        lien = '3.125.183.140/predict' + lien

        fetch(lien, {
                method: 'POST',
                body: JSON.stringify({ message: text1 }),
                mode: 'cors',
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
            })
            .then(r => r.json())
            .then(r => {
                let msg2 = { name: "Sam", message: r.answer };
                this.messages.push(msg2);
                this.updateChatText(chatbox)


                if (msg2.message.length < 500 && Langue != "Non") {
                    // console.log(document.querySelector('.active').innerText);
                    if ('speechSynthesis' in window) {
                        console.log('supported');
                    }else{
                        console.log('not supported');
                    }
                    textToAudio(Langue, msg2.message)
                }
                textField.value = ''

            }).catch((error) => {
                console.error('Error:', error);
                this.updateChatText(chatbox)
                textField.value = ''
            });

    }


    onSendButton(chatbox) {
        speechSynthesis.cancel();
        var textField = chatbox.querySelector('input');
        let text1 = textField.value.toLowerCase();
        textField.value = ''

        if (text1 === "" || text1 === " " || text1 === "aucun son") {
            return;
        }

        const etat = document.querySelector('.active').innerText;
        switch (etat) {
            case 'Français':
                this.sendChatText(chatbox, "Traitement en cours veuillez patienter⏳. Le temps d'attente dependra de votre connexion internet🌐🧑‍💻.");
                break;
            case 'English':
                this.sendChatText(chatbox, "Treatment in progress please wait⏳. The waiting time will depend on your internet🌐🧑 💻 connection.");
                break;
            case 'Español':
                this.sendChatText(chatbox, "Procesando en progreso por favor espere⏳. El tiempo de espera dependerá de tu conexión a internet🌐🧑‍💻.");
                break;
            case 'Deutsch':
                this.sendChatText(chatbox, "Bearbeitung läuft, bitte warten⏳. Die Wartezeit hängt von Ihrer Internetverbindung ab🌐🧑‍💻.");
                break;
            case 'Chinese':
                this.sendChatText(chatbox, "處理中請稍候⏳。 等待時間取決於您的網絡連接🌐🧑‍💻。");
                break;
            case 'Hausa':
                this.sendChatText(chatbox, "Ana ci gaba da aiwatarwa da fatan za a jira⏳. Lokacin jira zai dogara ne akan haɗin intanet ɗin ku🌐🧑‍💻.");
                break;
            case 'Igbo':
                this.sendChatText(chatbox, "Nhazi na-aga n'ihu, biko chere⏳. Oge nchere ga-adabere na njikọ ịntanetị gị🌐🧑‍💻.");
                break;
            case 'Yoruba':
                this.sendChatText(chatbox, "Ilọsiwaju lọwọ jọwọ duro⏳. Akoko idaduro yoo da lori asopọ intanẹẹti rẹ🌐🧑‍💻.");
                break;
            case 'Arabic':
                this.sendChatText(chatbox, "المعالجة جارية ، يرجى الانتظار⏳. سيعتمد وقت الانتظار على اتصالك بالإنترنت🌐🧑‍💻.");
                break;
            case 'Zulu':
                this.sendChatText(chatbox, "Ukucubungula kuyaqhubeka sicela ulinde⏳. Isikhathi sokulinda sizoncika ekuxhumekeni kwakho kwe-inthanethi🌐🧑‍💻.");
                break;
            case 'Russian':
                this.sendChatText(chatbox, "Идет обработка, пожалуйста, подождите⏳. Время ожидания будет зависеть от вашего интернет-соединения🌐🧑‍💻.");
                break;
            case 'Nyanja':
                this.sendChatText(chatbox, "Kukonza kuli mkati chonde dikirani⏳. Nthawi yodikirira idzatengera intaneti yanu🌐🧑‍💻.");
                break;
            case 'Italiano':
                this.sendChatText(chatbox, "Elaborazione in corso attendere⏳. Il tempo di attesa dipenderà dalla tua connessione internet🌐🧑‍💻.");
                break;
            case 'Creole':
                this.sendChatText(chatbox, "Pwosesis la ap fèt tanpri tann⏳. Tan ap tann lan pral depann de koneksyon entènèt ou🌐🧑‍💻.");
                break;
            case 'Hébreux':
                this.sendChatText(chatbox, "העיבוד מתבצע, אנא המתן⏳. זמן ההמתנה יהיה תלוי בחיבור האינטרנט שלך🌐🧑‍💻.");
                break;
            case 'Japonais':
                this.sendChatText(chatbox, "処理中です。しばらくお待ちください⏳。 待ち時間はインターネット接続状況によって異なります🌐🧑‍💻。");
                break;
            case 'Malagasy':
                this.sendChatText(chatbox, "Eo am-pikarakarana azafady ⏳. Ny fotoana fiandrasana dia hiankina amin'ny fifandraisanao amin'ny Internet🌐🧑‍💻.");
                break;
            case 'Soomaali':
                this.sendChatText(chatbox, "Howsha ayaa socota fadlan sug⏳. Waqtiga sugitaanka wuxuu ku xirnaan doonaa isku xirka interneedkaaga🌐🧑‍💻.");
                break;
            case 'Kiswahili':
                this.sendChatText(chatbox, "Inachakata tafadhali subiri⏳. Muda wa kusubiri utategemea muunganisho wako wa intaneti🌐🧑‍💻.");
                break;
            case 'Amharic':
                this.sendChatText(chatbox, "በሂደት ላይ ነው እባክዎ ይጠብቁ⏳። የጥበቃ ጊዜ በእርስዎ የበይነመረብ ግንኙነት🌐🧑‍💻 ይወሰናል።");
                break;
            case 'Hindi':
                this.sendChatText(chatbox, "प्रसंस्करण प्रगति पर है कृपया प्रतीक्षा करें⏳। प्रतीक्षा समय आपके इंटरनेट कनेक्शन पर निर्भर करेगा।");
                break;
            case 'Portuguese':
                this.sendChatText(chatbox, "Processamento em andamento, aguarde⏳. O tempo de espera dependerá da sua conexão com a internet🌐🧑‍💻.");
                break;
            default:
                this.sendChatText(chatbox, "Traitement en cours veuillez patienter⏳. Le temps d'attente dependra de votre connexion internet🌐🧑‍💻.");
                break;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        let lien = this.FindRoute()

        lien = '3.125.183.140/predict' + lien
        console.log(lien)

        fetch(lien, {
                method: 'POST',
                body: JSON.stringify({ message: text1 }),
                mode: 'cors',
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
            })
            .then(r => r.json())
            .then(r => {
                let msg2 = { name: "Sam", message: r.answer };
                this.messages.push(msg2);

                this.updateChatText(chatbox)

            }).catch((error) => {
                console.error('Error:', error);
                this.updateChatText(chatbox)
            });
    }

    onStart(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = ""
        fetch('3.125.183.140/start', {
                method: 'POST',
                body: JSON.stringify({ message: text1 }),
                mode: 'cors',
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
            })
            .then(r => r.json())
            .then(r => {
                let msg2 = { name: "Sam", message: r.answer };
                this.messages.push(msg2);

                this.updateChatText(chatbox)
                textField.value = ''

            }).catch((error) => {
                console.error('Error:', error);
                this.updateChatText(chatbox)
                textField.value = ''
            });
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Sam") {
                html += '<div class="messages__item messages__item--visitor"><img src="/static/images/chatbotGiova2.png" alt="image"><span class="tabulation"></span>' + item.message + '</div>'
            } else {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
        });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }

    sendChatText(chatbox, text) {
        var html = '';
        html += '<div class="messages__item messages__item--visitor"><img src="/static/images/chatbotGiova2.png" alt="image"><span class="tabulation"></span>' + text + '</div>'

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }

    FindRoute() {
        const langueMap = {
            "Français": "",
            "English": "Eng",
            "Español": "Esp",
            "Deutsch": "Deu",
            "Chinese": "Chn",
            "Hausa": "Hau",
            "Igbo": "Igb",
            "Yoruba": "Yor",
            "Arabic": "Ara",
            "Zulu": "Zul",
            "Russian": "Rus",
            "Nyanja": "Nya",
            "Italiano": "Ita",
            "Creole": "Cre",
            "Hébreux": "Heb",
            "Japonais": "Jap",
            "Malagasy": "Mal",
            "Soomaali": "Soo",
            "Kiswahili": "Kis",
            "Amharic": "Amh",
            "Hindi": "Hid",
            "Portuguese": "Por"
        };
        const langue = document.querySelector(".active").innerText;
         return langueMap[langue] || "";
        }
    }

const chatbox = new Chatbox();
chatbox.display();