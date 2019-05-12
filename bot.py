import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import os

const Discord = require('discord.js');
const client = new Discord.Client();

client.once('ready', () => {
	console.log('Ready!');
});

client.on('message', message => {
if (message.content === "=coinflip") {
    ballMessage = message.content.slice (0);
    number = 2;
    var random = Math.floor (Math.random() * (number - 1 + 1)) + 1;
    switch (random) {
        case 1: message.channel.send ('Heads'); break;
        case 2: message.channel.send ('Tails'); break;
    }
}
});

client.on('message', message => {
    if (message.content === "=status") {
        ballMessage = message.content.slice (0);
        number = 21;
        var random = Math.floor (Math.random() * (number - 1 + 1)) + 1;
        switch (random) {
            case 1: message.channel.send ('Battling Megatron.'); break;
            case 2: message.channel.send ('Eating at Shake Shack.'); break;
            case 3: message.channel.send ('Having a meeting with the United Servers of Discord members.'); break;
            case 4: message.channel.send ('Chillin at Pluto.'); break;
            case 5: message.channel.send ('Warping through a wormhole.'); break;
            case 6: message.channel.send ('Watching robo hentai.'); break;
            case 7: message.channel.send ('Playing Minecraft.'); break;
            case 8: message.channel.send ('Playing Diep.io.'); break;
            case 9: message.channel.send ('On a date with Cat Funt.'); break;
            case 10: message.channel.send ('Gathering Oil.'); break;
            case 11: message.channel.send ('Contemplating suicide.'); break;
            case 12: message.channel.send ('Smoking a gasoline flavored juul.'); break;
            case 13: message.channel.send ('Traveling to Korea.'); break;
            case 14: message.channel.send ('Traveling to Japan.'); break;
            case 15: message.channel.send ('Traveling to China.'); break;
            case 16: message.channel.send ('Trying to dodge taxes.'); break;
            case 17: message.channel.send ('Working at the Barber shop and giving someone the beam.'); break;
            case 18: message.channel.send ('Listening to the Gorillaz.'); break;
            case 19: message.channel.send ('In an epic battle with Godzilla.'); break;
            case 20: message.channel.send ('Looking for the All-Spark'); break;
            case 21: message.channel.send ('Fighting Iron-Man'); break;
        }
    }
    });

client.on('message', message => {
if (message.content.startsWith ("=compute:")) {
    ballMessage = message.content.slice (0);
    number = 69;
    var random = Math.floor (Math.random() * (number - 1 + 1)) + 1;
    switch (random) {
        case 1: message.channel.send ('Accoring to my calculations, the answer is no.'); break;
        case 2: message.channel.send ('My calculations say yes.'); break;
        case 3: message.channel.send ('This is a question that is best left unanswered.'); break;
        case 4: message.channel.send ('Quantum theory supports your statement.'); break;
        case 5: message.channel.send ('The laws of physics says your comment is "Wack as fuck".'); break;
        case 6: message.channel.send ('The theory of relativity disagrees with your words.'); break;
        case 7: message.channel.send ('Acient astrounut theorists...say yes.'); break;
        case 8: message.channel.send ('The NASA supercomputer Pleiades has evidence that backs up this remark'); break;
        case 9: message.channel.send ('The chess engine Stockfish believes you should "Make a move" out of this server with a hypothesis like that.'); break;
        case 10: message.channel.send ('If E=mc^2 then You=MassiveRetard for asking that question.'); break;
        case 11: message.channel.send ('Shut the fuck up I will fucking laser you with alien fucking eyes and explode your fucking head.'); break;
        case 12: message.channel.send ('Nigga I do not even need my computer for this shit. NO.'); break;
        case 13: message.channel.send ('Ask Stein instead idk bro.'); break;
        case 14: message.channel.send ('The future Cybertron is a stake if I answer this.'); break;
        case 15: message.channel.send ('You are not Ockie enough to ask such a question.'); break;
        case 16: message.channel.send ('Processing................................................................................................................................................................................................................................................................................................Yes.'); break;
        case 17: message.channel.send ('Yes, but only if you are high on nitroglycerin.'); break;
        case 18: message.channel.send ('Google would like to know your location.'); break;
        case 19: message.channel.send ('According to advanced Poker strategy, you can bet on it.'); break;
        case 20: message.channel.send ('Yes. By the way, I also got your results for you. You are pregnant. Congrats, what are you naming the baby?'); break;
        case 21: message.channel.send ('Magnum-Dongatron over at Pluto says no. However, he is a dick so ingore him.'); break;
        case 22: message.channel.send ('Sorry the United Servers of Discord requires I do not answer that question.'); break;
        case 23: message.channel.send ('Error 404.'); break;
        case 24: message.channel.send ('Elon Musk would say yes, due to the concept of equivalent exchange.'); break;
        case 25: message.channel.send ('Intresting question. Let us process this. First we must consider the Carbonaro Effect. In this effect, many unexplainable phenomenon happen, some of which involves items disappering. Now taking this into consideration, we can determine that Russia inventied the tech dech because those things disappered. And what country is know for making this disapper? Correct, Russia. So knowing Russia made the Tech Dech we now know Tony Hawk was Russian since he was the best skateboarder of all time. And since Tony Hawk is Russian, it tells us skateboards are advanced alein technology. Why? Because the asteroids always hit Russia, bringing alien materials to the area. So, insummary, Skateboards are alien technology made by Russian asteroids. This means that all skateboards are transformers. So, with all this data that we have collected, I can determine the answerto your question..........is no.'); break;
        case 26: message.channel.send ('Only Decepticons ask questions like that.'); break;
        case 27: message.channel.send ('By inverting the mobius strip I found that the answer to yur question is yes.'); break;
        case 28: message.channel.send ('Only in the matrix.'); break;
        case 29: message.channel.send ('I need a reference table to answer that question.'); break;
        case 30: message.channel.send ('My internet is down right now. Ask me later.'); break;
        case 31: message.channel.send ('This is an automated message from Spectrum. The use of the "=Compute" command has been block due to late bill payments. To use the "=Compute" command again, please contact Spectrum, or make your payments at a nearby Spectrum location.'); break;
        case 32: message.channel.send ('The Hubble Space Telescope can CLEARLY SEE that the answer is no.'); break;
        case 33: message.channel.send ('Since yu asked this question, on a scale of 1 to 10 how would you rate your brain damage?'); break;
        case 34: message.channel.send ('Sorry, the response is having trouble going through. Time until response: (4 decades)'); break;
        case 35: message.channel.send ('I have no clue bro. Just google it.'); break;
        case 36: message.channel.send ('To answer your quest- SHUT THE FUCK UP GIGALOAD I AM ANSWERING THIS NIGGAS QUESTION AND STOP EATING THE LEMONS YOU A ROBOT DUMBASS! To answer your question, yes.'); break;
        case 37: message.channel.send ('Yesnt'); break;
        case 38: message.channel.send ('According to a Buzzfeed quiz, you are a virgin. So I guess yeah...'); break;
        case 39: message.channel.send ('9/10 doctors say yes.'); break;
        case 40: message.channel.send ('The Theory of Everything states that everything you have said, it true.'); break;
        case 41: message.channel.send ('Your question is opinion based. I cannot answer this.'); break;
        case 42: message.channel.send ('Rose are red, violets are technically violet, yes bitch.'); break;
        case 43: message.channel.send ('If Curiosity is out there patrolling on Mars, then yes.'); break;
        case 44: message.channel.send ('My built in TI-84 plus calcuates that the answer is no.'); break;
        case 45: message.channel.send ('The Minecraft redstone computer says no.'); break;
        case 46: message.channel.send ('I believe you are not hydrated for asking such a question.'); break;
        case 47: message.channel.send ('You are not OCKIE enough to recieve an answer to that question. Do 100 push-ups and ask again.'); break;
        case 48: message.channel.send ('According t the Urban Dictionary, yes.'); break;
        case 50: message.channel.send ('Imbicule. Thoust shuld already know the answer to such a ludicrous question. It is no.'); break;
        case 51: message.channel.send ('Rick and Morty fan theory says yes.'); break;
        case 52: message.channel.send ('No, if you follow the guidlines from The Wolf of Wallstreet.'); break;
        case 53: message.channel.send ('Mark Zuckerberg requires I answer no.'); break;
        case 54: message.channel.send ('Bumbble Bee says "Yea Boi".'); break;
        case 55: message.channel.send ('I recommend you do not make such a statement unless you want to be sent to the shadow realm.'); break;
        case 56: message.channel.send ('Chistopher Columbus thought the earth was pear shaped so sure.'); break;
        case 57: message.channel.send ('Wikapedia says yes.'); break;
        case 58: message.channel.send ('Answers.com says no.'); break;
        case 59: message.channel.send ('The Twitter privacy policy requires that I answer no to prevent getting this profile deleted.'); break;
        case 60: message.channel.send ('BOT: Ockietron; is currently updating via Windows. Please wait and then ask again.'); break;
        case 61: message.channel.send ('According to the Mayan Calender, we should all be dead so who cares.'); break;
        case 62: message.channel.send ('According to the College Board, yes, but only if you have paid your tuition.'); break;
        case 63: message.channel.send ('No, but only if you are into K-pop'); break;
        case 64: message.channel.send ('ReferenceError: message is not defined AT: the part where your question made no fucking sense.'); break;
        case 65: message.channel.send ('I need the All-Spark to answer that question.'); break;
        case 66: message.channel.send ('This is a message from the United Servers of Discord: "FBI OPEN UP! WE ARE OUTSIDE YOUR DOOR!"'); break;
        case 67: message.channel.send ('Aerodynamics say yes.'); break;
        case 68: message.channel.send ('Based on Confucianism, yes.'); break;
        case 69: message.channel.send ('Congratulations. This is response #69. So no.'); break;
    }
}
});


client.run(str(os.environ.get('NTc2NTY0MTU1NzEzMDYwODY0.XNbEtQ.0QyVBuXiseDuofhz4BPOGsRSKVI')))
