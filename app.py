from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>💖 Harish - A Little Surprise 💖</title>

<style>

*{
    box-sizing:border-box;
}

body{
    margin:0;
    min-height:100vh;
    overflow:hidden;
    text-align:center;
    color:white;

    font-family:
    "Segoe UI",
    Tahoma,
    Arial,
    sans-serif;

    background:
    radial-gradient(circle at top,#ff9ecf,transparent 30%),
    radial-gradient(circle at bottom,#8a2be2,transparent 30%),
    linear-gradient(135deg,#160020,#4b164c,#b83280);
}

.page{
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    padding:20px;
}

.hidden{
    display:none !important;
}

.card{
    width:min(92%,720px);
    padding:35px 25px;
    border-radius:35px;

    background:rgba(255,255,255,.12);

    backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,.25);

    box-shadow:
    0 0 30px rgba(255,255,255,.15),
    0 0 60px rgba(255,105,180,.35);

    animation:cardIn 1s ease;
}

h1{
    font-family:
    Georgia,
    "Times New Roman",
    serif;

    font-size:44px;

    letter-spacing:2px;

    margin:12px;

    text-shadow:
    0 0 15px rgba(255,255,255,.7);
}

h2{
    font-size:29px;
    font-weight:500;
}

h3{
    font-size:20px;
}

p{
    font-size:18px;
    line-height:1.8;
}

button{
    border:none;

    padding:14px 27px;

    margin:10px;

    border-radius:30px;

    background:white;

    color:#b31362;

    font-size:17px;

    font-weight:bold;

    cursor:pointer;

    transition:.3s;
}

button:hover{
    transform:scale(1.08);

    box-shadow:
    0 0 15px white,
    0 0 30px #ff69b4;
}

.gift{
    font-size:110px;
    animation:bounce 1.5s infinite;
}

.lock{
    font-size:85px;
    animation:shake 1.5s infinite;
}

.icon{
    font-size:55px;
    animation:floatIcon 2s infinite;
}

.age{
    display:inline-block;

    padding:12px 25px;

    margin:10px;

    border-radius:25px;

    background:rgba(255,255,255,.18);

    font-size:24px;
}

.quote{
    font-family:Georgia,serif;

    font-style:italic;

    font-size:21px;

    color:#ffe7f3;
}

.heart{
    font-size:75px;

    animation:heart 1s infinite;
}

.cake{
    font-size:115px;

    animation:bounce 2s infinite;
}

.candles{
    font-size:42px;
}

.confetti{
    position:fixed;

    top:-30px;

    font-size:23px;

    animation:fall 4s linear forwards;

    z-index:10;
}

.balloon{
    position:fixed;

    bottom:-60px;

    font-size:40px;

    animation:up 7s linear forwards;

    z-index:5;
}

@keyframes cardIn{

    from{
        opacity:0;
        transform:scale(.8) translateY(30px);
    }

    to{
        opacity:1;
        transform:scale(1);
    }

}

@keyframes bounce{

    0%,100%{
        transform:translateY(0);
    }

    50%{
        transform:translateY(-20px);
    }

}

@keyframes shake{

    0%,100%{
        transform:rotate(0);
    }

    25%{
        transform:rotate(-10deg);
    }

    75%{
        transform:rotate(10deg);
    }

}

@keyframes floatIcon{

    50%{
        transform:translateY(-10px);
    }

}

@keyframes heart{

    50%{
        transform:scale(1.3);
    }

}

@keyframes fall{

    to{
        transform:
        translateY(110vh)
        rotate(700deg);
    }

}

@keyframes up{

    to{
        transform:
        translateY(-120vh);
    }

}

@media(max-width:600px){

    h1{
        font-size:31px;
    }

    h2{
        font-size:24px;
    }

    p{
        font-size:16px;
    }

    .card{
        padding:25px 18px;
    }

    .gift{
        font-size:90px;
    }

}

</style>

</head>

<body>


<!-- PAGE 1 -->

<div id="page1" class="page">

    <div class="gift">
        🎁
    </div>

    <div class="card">

        <div class="icon">
            ✨🤍✨
        </div>

        <h1>
            Hey Harish...
        </h1>

        <p>

            Idhu just oru normal birthday wish illa... 👀

            <br><br>

            Konjam different-ah,
            konjam special-ah,
            unakkaga mattum ready pannadhu. ✨

            <br><br>

            Why so special nu kekka koodadhu... 😌

            <br>

            Adhu oru secret. 🤫

        </p>

        <button onclick="openLock()">

            🎁 Secret-a Open Pannu

        </button>

    </div>

</div>



<!-- PAGE 2 -->

<div id="page2" class="page hidden">

    <div class="lock">
        🔐
    </div>

    <div class="card">

        <h1>
            One Small Test 😏
        </h1>

        <p>

            Un birthday date unakku theriyum la? 😂

            <br><br>

            Adha password-ah type pannu.

        </p>

        <input
            id="password"
            type="password"
            placeholder="Secret Password"
            style="
                width:270px;
                padding:15px;
                border:none;
                border-radius:20px;
                text-align:center;
                font-size:19px;
                outline:none;
            "
        >

        <br><br>

        <button onclick="unlock()">

            🔓 Unlock

        </button>

        <p>
            Hint: 🎂 DDMMYYYY
        </p>

    </div>

</div>



<!-- PAGE 3 -->

<div id="page3" class="page hidden">

    <div class="card">

        <div class="icon">
            😌✨🤍
        </div>

        <h1>
            Correct!
        </h1>

        <p>

            Seri... unlock pannita. 😏

            <br><br>

            Ippo konjam important-aana
            birthday wish irukku.

            <br><br>

            Read pannitu sirikka koodadhu 😂

        </p>

        <button onclick="birthdayPage()">

            ✨ Continue

        </button>

    </div>

</div>



<!-- PAGE 4 -->

<div id="page4" class="page hidden">

    <div class="card">

        <div class="icon">
            🎂✨
        </div>

        <h1>
            Happy Birthday Harish 🤍
        </h1>

        <div class="age">
            23 ✨
        </div>

        <h2>
            15.11.2026
        </h2>

        <p id="typing"></p>

        <button onclick="cakePage()">

            🎂 Next Surprise

        </button>

    </div>

</div>



<!-- PAGE 5 -->

<div id="page5" class="page hidden">

    <div class="card">

        <h1>
            Make a Wish ✨
        </h1>

        <div
            id="candles"
            class="candles"
        >
            🕯️ 🕯️ 🕯️ 🕯️ 🕯️
        </div>

        <div class="cake">
            🎂
        </div>

        <p>

            Kannai moodu... 👀

            <br><br>

            Unakku romba pidicha
            oru wish pannu. ✨

            <br><br>

            Maybe...

            <br>

            yaarukavadhu un smile
            romba important-ah irukkalaam. 😌

        </p>

        <button onclick="blowCandles()">

            🌬️ Blow Candles

        </button>

        <button onclick="finalPage()">

            🤍 Last Message

        </button>

    </div>

</div>



<!-- PAGE 6 -->

<div id="page6" class="page hidden">

    <div class="card">

        <div class="icon">
            ✨🤍✨
        </div>

        <h1>
            One Last Thing...
        </h1>

        <p>

            Harish,

            <br><br>

            Un life-la neraya people
            varalaam, pogalaam...

            <br><br>

            Aana sila people mattum
            reason illama special-ah
            feel aaguvanga.

            <br><br>

            Nee happy-ah irundha,
            adha paathu silent-ah happy
            aagura oruthar somewhere
            irukkaanga... 😌

            <br><br>

            Un smile eppovume
            ipdiye irukkanum.

            <br><br>

            Un dreams ellam
            true aaganum. ✨

            <br><br>

            And...

            <br><br>

            Unakku theriyama kooda,
            nee yaaroda life-la
            romba important person-ah
            irukkalaam. 🤍

        </p>

        <h2>

            Once Again,

            <br>

            Happy Birthday Harish 🎂✨

        </h2>

        <div class="heart">
            🤍
        </div>

        <p class="quote">

            "Some feelings don't need a name.
            They just stay special."

        </p>

    </div>

</div>



<script>


const message =
"Harish... innaiku un birthday. ✨ " +
"Unakku usual-a ellarum wish pannuvaanga. " +
"Aana indha wish konjam different. " +
"Un life-la nee nenacha ella vishayamum nadakkanum. " +
"Nee eppovume happy-ah irukkanum. " +
"Because... un smile yaarukko konjam extra special. 🤍";



function hideAll(){

    for(
        let i = 1;
        i <= 6;
        i++
    ){

        document
        .getElementById("page" + i)
        .classList
        .add("hidden");

    }

}



function openLock(){

    hideAll();

    document
    .getElementById("page2")
    .classList
    .remove("hidden");

}



function unlock(){

    let pass =
    document
    .getElementById("password")
    .value
    .trim();


    if(pass === "15112003"){

        hideAll();

        document
        .getElementById("page3")
        .classList
        .remove("hidden");

        confetti();

        balloons();

    }

    else{

        alert(
            "😂 Wrong password!\n\n" +
            "Birthday date-ah yosichu paaru 🎂"
        );

    }

}



function birthdayPage(){

    hideAll();

    document
    .getElementById("page4")
    .classList
    .remove("hidden");

    typeMessage();

    confetti();

    balloons();

}



function typeMessage(){

    let box =
    document
    .getElementById("typing");

    box.innerHTML = "";

    let i = 0;


    function type(){

        if(i < message.length){

            box.innerHTML +=
            message.charAt(i);

            i++;

            setTimeout(
                type,
                40
            );

        }

    }

    type();

}



function cakePage(){

    hideAll();

    document
    .getElementById("page5")
    .classList
    .remove("hidden");

    confetti();

}



function blowCandles(){

    document
    .getElementById("candles")
    .innerHTML =
    "💨 ✨ 💨 ✨ 💨";

    confetti();

    setTimeout(
        function(){

            alert(
                "Wish pannitiya? 😌✨\n\n" +
                "Hopefully adhu seekiram true aagum 🤍"
            );

        },
        300
    );

}



function finalPage(){

    hideAll();

    document
    .getElementById("page6")
    .classList
    .remove("hidden");

    confetti();

    balloons();

}



function confetti(){

    let items = [

        "✨",
        "🤍",
        "🎉",
        "🌸",
        "⭐",
        "💫",
        "🎈"

    ];


    for(
        let i = 0;
        i < 80;
        i++
    ){

        let x =
        document.createElement("div");

        x.className =
        "confetti";

        x.innerHTML =
        items[
            Math.floor(
                Math.random()
                * items.length
            )
        ];

        x.style.left =
        Math.random()
        * 100
        + "vw";

        x.style.animationDuration =
        (2 + Math.random() * 3)
        + "s";

        document.body.appendChild(x);


        setTimeout(
            function(){

                x.remove();

            },
            6000
        );

    }

}



function balloons(){

    for(
        let i = 0;
        i < 8;
        i++
    ){

        let b =
        document.createElement("div");

        b.className =
        "balloon";

        b.innerHTML =
        "🎈";

        b.style.left =
        (5 + i * 12)
        + "vw";

        b.style.animationDelay =
        (i * .3)
        + "s";

        document.body.appendChild(b);


        setTimeout(
            function(){

                b.remove();

            },
            8000
        );

    }

}

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True)