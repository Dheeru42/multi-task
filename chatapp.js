import OpenAI from 'openai';

// readline js
import * as readline from 'node:readline/promises'; // js
import { stdin as input, stdout as output } from 'node:process'; // js

const rl = readline.createInterface({ input, output }); // js

const messages = [] // global declare

console.log("Welcome To RAM CHAT")
const key = process.env['API_KEY']

// openai js
const openai = new OpenAI({
  apiKey: key, // defaults to process.env["OPENAI_API_KEY"]
});

async function main(input) {
  messages.push({ role: 'user', content: input })               
  const chatCompletion = await openai.chat.completions.create({
    messages: messages,
    model: 'gpt-3.5-turbo',
  });

  //console.log(chatCompletion.choices);
  console.log(chatCompletion.choices[0]?.message?.content);
}

//main();
// readline js
rl.on('line', (input) => {
  console.log(`Received: ${input}`);
  main(input)
  if(input=="q")
  {rl.close();}
}); 
