"""EasyFin, powered by NYZTrade. SINGLE FILE VERSION with Malayalam (app.py + requirements.txt only)."""
import os as _os
import sys as _sys
import types as _types

import hashlib as _hl
_SOURCES = {}
_SOURCES['more_data_seed'] = r'''"""Extra Seedlings questions, English and Malayalam side by side (draft: please review).
Each item: (question, [options], right_index, why, ml_question, [ml_options], ml_why). Options keep the same order in both languages."""

DATA = {
"s1": [
 ('Which coin is worth the least?', ['₹1 coin', '₹2 coin', '₹5 coin'], 0, '1 is the smallest number.',
  'ഏറ്റവും വില കുറഞ്ഞ നാണയം ഏതാ?', ['₹1 നാണയം', '₹2 നാണയം', '₹5 നാണയം'], '1 ആണ് ഏറ്റവും ചെറിയ സംഖ്യ.'),
 ('How many ₹2 coins make ₹10?', ['2', '5', '10'], 1, '2 times 5 is 10.',
  '₹10 ആകാൻ എത്ര ₹2 നാണയം വേണം?', ['2', '5', '10'], '2 നെ 5 പ്രാവശ്യം കൂട്ടിയാൽ 10.'),
 ('A ₹10 note and a ₹5 coin together make...', ['₹15', '₹105', '₹5'], 0, '10 plus 5 is 15.',
  'ഒരു ₹10 നോട്ടും ഒരു ₹5 നാണയവും കൂടിയാൽ...', ['₹15', '₹105', '₹5'], '10 ഉം 5 ഉം കൂടിയാൽ 15.'),
 ('You have ₹5. A ₹10 note is...', ['Worth more', 'Worth less', 'Worth the same'], 0, '10 is more than 5.',
  'നിന്റെ കൈയിൽ ₹5 ഉണ്ട്. ഒരു ₹10 നോട്ട്...', ['കൂടുതൽ വിലയുള്ളതാ', 'കുറഞ്ഞ വിലയുള്ളതാ', 'അതേ വിലയുള്ളതാ'], '10 എന്നത് 5 നെക്കാൾ കൂടുതലാ.'),
 ('What do shops give you when you pay more than the price?', ['Change', 'A bill only', 'Nothing'], 0, 'Change is the money given back.',
  'വിലയെക്കാൾ കൂടുതൽ കൊടുത്താൽ കടക്കാരൻ എന്താ തിരിച്ചു തരുന്നത്?', ['ബാക്കി പൈസ', 'ബിൽ മാത്രം', 'ഒന്നുമില്ല'], 'തിരിച്ചു തരുന്ന പൈസയാണ് ബാക്കി.'),
 ('Which of these is a paper note?', ['₹100', '₹1', '₹2'], 0, '₹1 and ₹2 are coins. ₹100 is a note.',
  'ഇതിൽ കടലാസ് നോട്ട് ഏതാ?', ['₹100', '₹1', '₹2'], '₹1 ഉം ₹2 ഉം നാണയങ്ങളാ. ₹100 ഒരു നോട്ടാ.'),
 ('Two ₹10 notes make how much?', ['₹20', '₹12', '₹102'], 0, '10 plus 10 is 20.',
  'രണ്ട് ₹10 നോട്ട് കൂടിയാൽ എത്ര?', ['₹20', '₹12', '₹102'], '10 ഉം 10 ഉം കൂടിയാൽ 20.'),
 ('A ₹5 coin and a ₹2 coin together make...', ['₹7', '₹52', '₹3'], 0, '5 plus 2 is 7.',
  'ഒരു ₹5 നാണയവും ഒരു ₹2 നാണയവും കൂടിയാൽ...', ['₹7', '₹52', '₹3'], '5 ഉം 2 ഉം കൂടിയാൽ 7.'),
 ('How many ₹5 coins make ₹20?', ['2', '4', '20'], 1, '5 times 4 is 20.',
  '₹20 ആകാൻ എത്ര ₹5 നാണയം വേണം?', ['2', '4', '20'], '5 നെ 4 പ്രാവശ്യം കൂട്ടിയാൽ 20.'),
 ('Which is more money?', ['₹20', '₹15', 'They are the same'], 0, '20 is more than 15.',
  'ഏതാ കൂടുതൽ പൈസ?', ['₹20', '₹15', 'രണ്ടും ഒരുപോലെ'], '20 എന്നത് 15 നെക്കാൾ കൂടുതലാ.'),
 ('To pay ₹7 you can use a ₹5 coin and...', ['A ₹2 coin', 'A ₹1 coin', 'A ₹10 note'], 0, '5 plus 2 is 7.',
  '₹7 കൊടുക്കാൻ ഒരു ₹5 നാണയത്തിന്റെ കൂടെ എന്താ വേണ്ടത്?', ['ഒരു ₹2 നാണയം', 'ഒരു ₹1 നാണയം', 'ഒരു ₹10 നോട്ട്'], '5 ഉം 2 ഉം കൂടിയാൽ 7.'),
 ('Why do we count money carefully?', ['To avoid mistakes', 'To waste time', 'To hide it'], 0, 'Careful counting stops mistakes.',
  'നമ്മൾ പൈസ ശ്രദ്ധിച്ച് എണ്ണുന്നത് എന്തിനാ?', ['തെറ്റ് വരാതിരിക്കാൻ', 'സമയം കളയാൻ', 'ഒളിപ്പിക്കാൻ'], 'ശ്രദ്ധിച്ച് എണ്ണിയാൽ തെറ്റ് വരില്ല.'),
 ('A ₹50 note is worth how many ₹10 notes?', ['5', '10', '50'], 0, '10 times 5 is 50.',
  'ഒരു ₹50 നോട്ട് എത്ര ₹10 നോട്ടിന് തുല്യമാ?', ['5', '10', '50'], '10 നെ 5 പ്രാവശ്യം കൂട്ടിയാൽ 50.'),
],
"s2": [
 ('A school bag is a...', ['Need', 'Want', 'Toy'], 0, 'We need it to carry our books.',
  'ഒരു സ്കൂൾ ബാഗ് ഒരു...', ['ആവശ്യം', 'ആഗ്രഹം', 'കളിപ്പാട്ടം'], 'പുസ്തകം കൊണ്ടുപോകാൻ നമുക്കത് വേണം.'),
 ('Which of these is a want?', ['A chocolate bar', 'Rice', 'Drinking water'], 0, 'We can live without chocolate.',
  'ഇതിൽ ഏതാ ഒരു ആഗ്രഹം?', ['ഒരു ചോക്ലേറ്റ്', 'അരി', 'കുടിവെള്ളം'], 'ചോക്ലേറ്റ് ഇല്ലെങ്കിലും നമുക്ക് ജീവിക്കാം.'),
 ('A raincoat in the monsoon is a...', ['Need', 'Want', 'Game'], 0, 'It keeps us dry and healthy.',
  'മഴക്കാലത്തെ ഒരു റെയിൻകോട്ട് ഒരു...', ['ആവശ്യം', 'ആഗ്രഹം', 'കളി'], 'അത് നമ്മളെ നനയാതെയും അസുഖം വരാതെയും കാക്കും.'),
 ('A fancy toy robot is a...', ['Want', 'Need', 'Medicine'], 0, 'Toys are fun, but we do not need them to live.',
  'ഭംഗിയുള്ള ഒരു കളിപ്പാട്ട റോബോട്ട് ഒരു...', ['ആഗ്രഹം', 'ആവശ്യം', 'മരുന്ന്'], 'കളിപ്പാട്ടം രസമാ, പക്ഷേ ജീവിക്കാൻ അത് വേണ്ട.'),
 ('Which is a need for a baby?', ['Milk', 'A balloon', 'A cartoon sticker'], 0, 'Babies need milk to grow.',
  'ഒരു കുഞ്ഞിന് ആവശ്യമുള്ളത് ഏതാ?', ['പാൽ', 'ഒരു ബലൂൺ', 'ഒരു കാർട്ടൂൺ സ്റ്റിക്കർ'], 'വളരാൻ കുഞ്ഞുങ്ങൾക്ക് പാൽ വേണം.'),
 ('Your friend has a new gadget. Do you need it too?', ['No, it is a want', 'Yes, always', 'Only if it is red'], 0, 'Wanting what a friend has is not the same as needing it.',
  'നിന്റെ കൂട്ടുകാരന് ഒരു പുതിയ ഗാഡ്ജറ്റ് ഉണ്ട്. നിനക്കും അത് വേണോ?', ['വേണ്ട, അത് ഒരു ആഗ്രഹം മാത്രമാ', 'വേണം, എപ്പോഴും', 'ചുവപ്പ് ആണെങ്കിൽ മാത്രം'], 'കൂട്ടുകാരന് ഉണ്ട് എന്ന് കരുതി നമുക്കും വേണം എന്നില്ല.'),
 ('Which is a need?', ['A safe place to sleep', 'A toy castle', 'A comic book'], 0, 'Everyone needs a safe place to rest.',
  'ഇതിൽ ആവശ്യം ഏതാ?', ['ഉറങ്ങാൻ സേഫായ ഒരിടം', 'ഒരു കളിപ്പാട്ട കൊട്ടാരം', 'ഒരു കോമിക് ബുക്ക്'], 'എല്ലാവർക്കും വിശ്രമിക്കാൻ സേഫായ ഒരിടം വേണം.'),
 ('You have ₹50. What do you buy first?', ['A notebook for school', 'A sticker pack', 'Neither'], 0, 'Needs come before wants.',
  'നിന്റെ കൈയിൽ ₹50 ഉണ്ട്. ആദ്യം എന്ത് വാങ്ങും?', ['സ്കൂളിലേക്കുള്ള ഒരു നോട്ടുബുക്ക്', 'ഒരു സ്റ്റിക്കർ പായ്ക്ക്', 'രണ്ടും വേണ്ട'], 'ആഗ്രഹത്തിന് മുൻപ് ആവശ്യം.'),
 ('New shoes when your old ones are torn are a...', ['Need', 'Want', 'Toy'], 0, 'We need shoes to protect our feet.',
  'പഴയ ചെരിപ്പ് പൊട്ടിയപ്പോൾ വാങ്ങുന്ന പുതിയ ചെരിപ്പ് ഒരു...', ['ആവശ്യം', 'ആഗ്രഹം', 'കളിപ്പാട്ടം'], 'കാല് സംരക്ഷിക്കാൻ നമുക്ക് ചെരിപ്പ് വേണം.'),
 ('A party hat is a...', ['Want', 'Need', 'Medicine'], 0, 'It is fun, not a must.',
  'ഒരു പാർട്ടി തൊപ്പി ഒരു...', ['ആഗ്രഹം', 'ആവശ്യം', 'മരുന്ന്'], 'അത് രസത്തിനാ, നിർബന്ധമൊന്നുമില്ല.'),
 ('True or false: wants can sometimes wait.', ['True', 'False', 'Only on Sundays'], 0, 'We can plan and wait for wants.',
  'ശരിയോ തെറ്റോ: ആഗ്രഹങ്ങൾക്ക് ചിലപ്പോൾ കാത്തിരിക്കാം.', ['ശരി', 'തെറ്റ്', 'ഞായറാഴ്ച മാത്രം'], 'പ്ലാൻ ചെയ്ത് ആഗ്രഹങ്ങൾക്ക് കാത്തിരിക്കാം.'),
 ('Which pair has one need and one want?', ['Water and ice cream', 'Rice and water', 'Toy and game'], 0, 'Water is a need. Ice cream is a want.',
  'ഏത് ജോഡിയിലാ ഒരു ആവശ്യവും ഒരു ആഗ്രഹവും ഉള്ളത്?', ['വെള്ളവും ഐസ്ക്രീമും', 'അരിയും വെള്ളവും', 'കളിപ്പാട്ടവും ഗെയിമും'], 'വെള്ളം ആവശ്യമാ. ഐസ്ക്രീം ആഗ്രഹമാ.'),
 ("A doctor's visit when you are very sick is a...", ['Need', 'Want', 'Treat'], 0, 'Getting well is a need.',
  'നല്ല അസുഖം വരുമ്പോൾ ഡോക്ടറെ കാണുന്നത് ഒരു...', ['ആവശ്യം', 'ആഗ്രഹം', 'ട്രീറ്റ്'], 'അസുഖം മാറുക എന്നത് ആവശ്യമാ.'),
],
"s3": [
 ('Pinku saves ₹10 each week. How many weeks to save ₹40?', ['4', '10', '40'], 0, '10 times 4 is 40.',
  'പിങ്കു ആഴ്ചയിൽ ₹10 വീതം സമ്പാദിക്കും. ₹40 ആകാൻ എത്ര ആഴ്ച വേണം?', ['4', '10', '40'], '10 നെ 4 പ്രാവശ്യം കൂട്ടിയാൽ 40.'),
 ('You have ₹15 saved and add ₹5. How much now?', ['₹20', '₹10', '₹155'], 0, '15 plus 5 is 20.',
  'നിന്റെ കൈയിൽ ₹15 സമ്പാദ്യം ഉണ്ട്, ₹5 കൂടി ഇടുന്നു. ഇപ്പോൾ എത്ര ഉണ്ട്?', ['₹20', '₹10', '₹155'], '15 ഉം 5 ഉം കൂടിയാൽ 20.'),
 ('A goal is...', ['Something you want to reach', 'A kind of coin', 'A shop'], 0, 'A goal is what you are saving for.',
  'ലക്ഷ്യം എന്നാൽ...', ['എത്തിപ്പിടിക്കാൻ ആഗ്രഹിക്കുന്ന കാര്യം', 'ഒരു തരം നാണയം', 'ഒരു കട'], 'നീ എന്തിനാണോ സമ്പാദിക്കുന്നത്, അതാ ലക്ഷ്യം.'),
 ('Pinku wants a ₹20 book and saves ₹4 a day. How many days?', ['5', '4', '20'], 0, '4 times 5 is 20.',
  'പിങ്കുവിന് ₹20 ന്റെ പുസ്തകം വേണം, ദിവസവും ₹4 സമ്പാദിക്കും. എത്ര ദിവസം വേണം?', ['5', '4', '20'], '4 നെ 5 പ്രാവശ്യം കൂട്ടിയാൽ 20.'),
 ('Saving ₹1 a day for 7 days gives...', ['₹7', '₹17', '₹1'], 0, '1 times 7 is 7.',
  'ദിവസവും ₹1 വീതം 7 ദിവസം സമ്പാദിച്ചാൽ...', ['₹7', '₹17', '₹1'], '1 നെ 7 പ്രാവശ്യം കൂട്ടിയാൽ 7.'),
 ('What helps your piggy bank fill up?', ['Adding a little every day', 'Opening it every hour', 'Spending the coins'], 0, 'Small, regular saving adds up.',
  'കുടുക്ക നിറയാൻ എന്താ സഹായിക്കുക?', ['ദിവസവും കുറച്ച് കുറച്ച് ഇടുക', 'ഓരോ മണിക്കൂറും തുറന്ന് നോക്കുക', 'നാണയം എടുത്ത് ചെലവാക്കുക'], 'ചെറിയ തുകകൾ സ്ഥിരമായി ഇട്ടാൽ കൂടിക്കൂടി വരും.'),
 ('Your piggy bank has ₹30 and you take out ₹10 for a treat. How much is left?', ['₹20', '₹40', '₹10'], 0, '30 minus 10 is 20.',
  'നിന്റെ കുടുക്കയിൽ ₹30 ഉണ്ട്, ഒരു ട്രീറ്റിന് ₹10 എടുത്തു. എത്ര ബാക്കി?', ['₹20', '₹40', '₹10'], '30 ൽ നിന്ന് 10 പോയാൽ 20.'),
 ('Why break a big goal into small steps?', ['It feels easier to reach', 'It costs more', 'So you forget it'], 0, 'Small steps feel doable.',
  'വലിയ ലക്ഷ്യത്തെ ചെറിയ സ്റ്റെപ്പുകളായി ഭാഗിക്കുന്നത് എന്തിനാ?', ['എത്താൻ എളുപ്പം തോന്നും', 'അതിന് കൂടുതൽ ചെലവാകും', 'മറന്നുപോകാൻ'], 'ചെറിയ സ്റ്റെപ്പുകൾ ചെയ്യാൻ എളുപ്പം തോന്നും.'),
 ('You save ₹5 every day. How much after 2 days?', ['₹10', '₹7', '₹52'], 0, '5 times 2 is 10.',
  'നീ ദിവസവും ₹5 വീതം സമ്പാദിക്കും. 2 ദിവസം കഴിഞ്ഞാൽ എത്ര?', ['₹10', '₹7', '₹52'], '5 നെ 2 പ്രാവശ്യം കൂട്ടിയാൽ 10.'),
 ('Where should a piggy bank stay?', ['In a safe place at home', 'On the street', "At a stranger's house"], 0, 'Keep it where only your family can reach it.',
  'കുടുക്ക എവിടെയാ വെക്കേണ്ടത്?', ['വീട്ടിലെ സേഫായ സ്ഥലത്ത്', 'റോഡിൽ', 'ഒരു അപരിചിതന്റെ വീട്ടിൽ'], 'വീട്ടുകാർക്ക് മാത്രം എത്താൻ പറ്റുന്ന സ്ഥലത്ത് വെക്കണം.'),
 ('Meera spends all her money. Pinku saves some. Who can buy a ₹20 gift later?', ['Pinku', 'Meera', 'Nobody'], 0, 'Saved money is there when you need it.',
  'മീര കിട്ടുന്ന പൈസ മുഴുവൻ ചെലവാക്കും. പിങ്കു കുറച്ച് സമ്പാദിക്കും. പിന്നീട് ₹20 ന്റെ സമ്മാനം ആർക്ക് വാങ്ങാൻ പറ്റും?', ['പിങ്കുവിന്', 'മീരയ്ക്ക്', 'ആർക്കും പറ്റില്ല'], 'സമ്പാദിച്ച പൈസ ആവശ്യം വരുമ്പോൾ കൈയിൽ ഉണ്ടാകും.'),
 ('What do you need most to save for a long time?', ['Patience', 'Speed', 'Luck'], 0, 'Saving takes time and patience.',
  'ഒരുപാട് കാലം സമ്പാദിക്കാൻ ഏറ്റവും വേണ്ടത് എന്താ?', ['ക്ഷമ', 'സ്പീഡ്', 'ഭാഗ്യം'], 'സമ്പാദിക്കാൻ സമയവും ക്ഷമയും വേണം.'),
 ('A goal costs ₹100 and you have ₹60. How much more do you need?', ['₹40', '₹60', '₹160'], 0, '100 minus 60 is 40.',
  'ഒരു ലക്ഷ്യത്തിന് ₹100 വേണം, നിന്റെ കൈയിൽ ₹60 ഉണ്ട്. ഇനി എത്ര വേണം?', ['₹40', '₹60', '₹160'], '100 ൽ നിന്ന് 60 പോയാൽ 40.'),
],
"s4": [
 ('A baker sells bread. This is...', ['Work', 'A gift', 'A game'], 0, 'Selling what you make is work.',
  'ഒരു ബേക്കർ റൊട്ടി വിൽക്കുന്നു. ഇത്...', ['ജോലി', 'ഒരു സമ്മാനം', 'ഒരു കളി'], 'ഉണ്ടാക്കിയത് വിൽക്കുന്നത് ഒരു ജോലിയാ.'),
 ('Who earns money by growing rice?', ['A farmer', 'A cloud', 'A toy'], 0, 'Farmers sell what they grow.',
  'നെല്ല് കൃഷി ചെയ്ത് പൈസ ഉണ്ടാക്കുന്നത് ആരാ?', ['ഒരു കർഷകൻ', 'ഒരു മേഘം', 'ഒരു കളിപ്പാട്ടം'], 'കർഷകർ വിളയിച്ചത് വിൽക്കും.'),
 ('A fisherman sells fish. He...', ['Earns money from his work', 'Gets a gift', 'Loses money'], 0, 'Selling the catch is how he earns.',
  'ഒരു മത്സ്യത്തൊഴിലാളി മീൻ വിൽക്കുന്നു. അദ്ദേഹം...', ['ജോലി ചെയ്ത് പൈസ ഉണ്ടാക്കുന്നു', 'ഒരു സമ്മാനം നേടുന്നു', 'പൈസ കളയുന്നു'], 'പിടിച്ച മീൻ വിൽക്കുന്നതാണ് അദ്ദേഹത്തിന്റെ വരുമാനം.'),
 ('Money from grandparents on your birthday is...', ['A gift', 'A salary', 'A fine'], 0, 'Gifts come from love, not from work.',
  'പിറന്നാളിന് മുത്തശ്ശനും മുത്തശ്ശിയും തരുന്ന പൈസ...', ['ഒരു സമ്മാനമാ', 'ഒരു ശമ്പളമാ', 'ഒരു പിഴയാ'], 'സമ്മാനം സ്നേഹം കൊണ്ട് തരുന്നതാ, ജോലിക്ക് തരുന്നതല്ല.'),
 ('A tailor stitches clothes. How does the tailor earn?', ['Customers pay for the clothes', 'Trees give money', 'Birds bring money'], 0, 'People pay for useful work.',
  'ഒരു തയ്യൽക്കാരൻ ഉടുപ്പ് തയ്ക്കുന്നു. അദ്ദേഹത്തിന് പൈസ എങ്ങനെ കിട്ടും?', ['കസ്റ്റമേഴ്സ് ഉടുപ്പിന് പൈസ കൊടുക്കും', 'മരം പൈസ തരും', 'പക്ഷികൾ പൈസ കൊണ്ടുവരും'], 'ഉപകാരമുള്ള പണിക്ക് ആളുകൾ പൈസ കൊടുക്കും.'),
 ('Which one is work?', ['A driver takes passengers', 'A friend gives you a toy', 'You find a feather'], 0, 'Driving passengers is a job.',
  'ഇതിൽ ജോലി ഏതാ?', ['ഒരു ഡ്രൈവർ യാത്രക്കാരെ കൊണ്ടുപോകുന്നു', 'ഒരു കൂട്ടുകാരൻ കളിപ്പാട്ടം തരുന്നു', 'നിനക്ക് ഒരു തൂവൽ കിട്ടുന്നു'], 'യാത്രക്കാരെ കൊണ്ടുപോകുന്നത് ഒരു ജോലിയാ.'),
 ('You earn ₹10 from each of 3 customers. How much in all?', ['₹30', '₹13', '₹103'], 0, '10 times 3 is 30.',
  '3 കസ്റ്റമേഴ്സിൽ നിന്ന് ഓരോരുത്തരിൽ നിന്നും ₹10 കിട്ടുന്നു. ആകെ എത്ര?', ['₹30', '₹13', '₹103'], '10 നെ 3 പ്രാവശ്യം കൂട്ടിയാൽ 30.'),
 ('A nurse earns by...', ['Caring for sick people', 'Selling toys', 'Driving a bus'], 0, 'Nurses help patients get well.',
  'ഒരു നഴ്സിന് പൈസ കിട്ടുന്നത്...', ['രോഗികളെ നോക്കിയിട്ട്', 'കളിപ്പാട്ടം വിറ്റിട്ട്', 'ബസ് ഓടിച്ചിട്ട്'], 'രോഗികൾ സുഖം പ്രാപിക്കാൻ നഴ്സുമാർ സഹായിക്കും.'),
 ('A gift is...', ['Given freely', 'Always pay for work', 'Always given back'], 0, 'A gift is not payment.',
  'ഒരു സമ്മാനം എന്നാൽ...', ['ഫ്രീ ആയി തരുന്നത്', 'ജോലിക്കുള്ള കൂലി എപ്പോഴും', 'എപ്പോഴും തിരിച്ചു കൊടുക്കേണ്ടത്'], 'സമ്മാനം കൂലിയല്ല.'),
 ('Why is it good to earn money honestly?', ['It is fair and makes us proud', 'It is faster to take it', 'Nobody notices'], 0, 'Honest work is fair to everyone.',
  'സത്യസന്ധമായി പൈസ ഉണ്ടാക്കുന്നത് നല്ലതാകുന്നത് എന്തുകൊണ്ടാ?', ['അത് ന്യായമാ, നമുക്ക് അഭിമാനം തോന്നും', 'എടുക്കുന്നതാ എളുപ്പം', 'ആരും അറിയില്ല'], 'സത്യസന്ധമായ ജോലി എല്ലാവരോടും ന്യായമാ.'),
 ("A child waters the neighbours' plants and they say thanks. Is it always paid?", ['No, helping can be kindness', 'Yes, always', 'Only on Fridays'], 0, 'Helping can come from kindness, not only pay.',
  'ഒരു കുട്ടി അയൽക്കാരുടെ ചെടിക്ക് വെള്ളം ഒഴിക്കുന്നു, അവർ താങ്ക്സ് പറയുന്നു. ഇതിന് എപ്പോഴും പൈസ കിട്ടുമോ?', ['ഇല്ല, സഹായിക്കുന്നത് സ്നേഹം കൊണ്ടും ആകാം', 'കിട്ടും, എപ്പോഴും', 'വെള്ളിയാഴ്ച മാത്രം'], 'സഹായം സ്നേഹത്തിൽ നിന്നും വരാം, കൂലിക്ക് വേണ്ടി മാത്രമല്ല.'),
 ('Which one is NOT earning?', ["Taking money from someone's bag", 'Selling juice', 'Teaching a class'], 0, 'Taking what is not yours is wrong.',
  'ഇതിൽ പൈസ ഉണ്ടാക്കൽ അല്ലാത്തത് ഏതാ?', ['ആരുടെയെങ്കിലും ബാഗിൽ നിന്ന് പൈസ എടുക്കുന്നത്', 'ജ്യൂസ് വിൽക്കുന്നത്', 'ക്ലാസ്സെടുക്കുന്നത്'], 'നമ്മുടേതല്ലാത്തത് എടുക്കുന്നത് തെറ്റാ.'),
 ('A potter makes pots and sells them. This is...', ['Earning from a craft', 'A gift', 'A prize'], 0, 'Making and selling is honest work.',
  'ഒരു കുശവൻ കലം ഉണ്ടാക്കി വിൽക്കുന്നു. ഇത്...', ['കൈത്തൊഴിൽ ചെയ്ത് കിട്ടുന്ന വരുമാനം', 'ഒരു സമ്മാനം', 'ഒരു പ്രൈസ്'], 'ഉണ്ടാക്കി വിൽക്കുന്നത് സത്യസന്ധമായ ജോലിയാ.'),
],
"s5": [
 ('Sharing a toy with your sibling is...', ['Kind', 'Unkind', 'A waste'], 0, 'Sharing shows care.',
  'കൂടപ്പിറപ്പിനോട് കളിപ്പാട്ടം പങ്കുവെക്കുന്നത്...', ['നല്ല കാര്യമാ', 'നല്ലതല്ല', 'വെറുതെയാ'], 'പങ്കുവെക്കുന്നത് സ്നേഹം കാണിക്കുന്നു.'),
 ('A new student has no pencil. You can...', ['Lend yours', 'Ignore them', 'Laugh at them'], 0, 'A small help makes a friend.',
  'പുതിയതായി വന്ന ഒരു കുട്ടിക്ക് പെൻസിൽ ഇല്ല. നിനക്ക്...', ['നിന്റേത് കടം കൊടുക്കാം', 'മൈൻഡ് ചെയ്യാതിരിക്കാം', 'കളിയാക്കാം'], 'ചെറിയ ഒരു സഹായം ഒരു കൂട്ടുകാരനെ തരും.'),
 ('Which makes you a good friend?', ['Sharing and caring', 'Teasing', 'Grabbing'], 0, 'Good friends share and care.',
  'ഒരു നല്ല കൂട്ടുകാരനാക്കുന്നത് എന്താ?', ['പങ്കുവെക്കലും കരുതലും', 'കളിയാക്കൽ', 'പിടിച്ചുപറിക്കൽ'], 'നല്ല കൂട്ടുകാർ പങ്കുവെക്കും, കരുതുകയും ചെയ്യും.'),
 ('Money in a charity box is used to...', ['Help people in need', 'Pay for the box', 'Buy sweets for one person'], 0, 'Charity is for helping others.',
  'ദാനപ്പെട്ടിയിലെ പൈസ എന്തിനാ ഉപയോഗിക്കുന്നത്?', ['ആവശ്യമുള്ളവരെ സഹായിക്കാൻ', 'പെട്ടിക്ക് പൈസ കൊടുക്കാൻ', 'ഒരാൾക്ക് മാത്രം മധുരം വാങ്ങാൻ'], 'ദാനം മറ്റുള്ളവരെ സഹായിക്കാനുള്ളതാ.'),
 ('Which is the best thing to share?', ['Kindness', 'Anger', 'Lies'], 0, 'Kindness grows when we share it.',
  'പങ്കുവെക്കാൻ ഏറ്റവും നല്ലത് ഏതാ?', ['സ്നേഹം', 'ദേഷ്യം', 'നുണകൾ'], 'പങ്കുവെക്കുമ്പോൾ സ്നേഹം വളരും.'),
 ('You have 4 sweets and share equally with a friend. How many does each get?', ['2', '4', '1'], 0, '4 shared between 2 is 2 each.',
  'നിനക്ക് 4 മധുരം ഉണ്ട്, കൂട്ടുകാരനുമായി സമമായി പങ്കിടുന്നു. ഓരോരുത്തർക്കും എത്ര കിട്ടും?', ['2', '4', '1'], '4 നെ രണ്ടുപേർ പങ്കിട്ടാൽ ഓരോരുത്തർക്കും 2.'),
 ('At festivals like Onam, Eid and Christmas, sharing means...', ['Giving some food or treats to others', 'Eating alone', 'Hiding the sweets'], 0, 'Festivals are happier when we share.',
  'ഓണം, പെരുന്നാൾ, ക്രിസ്മസ് പോലുള്ള ആഘോഷങ്ങളിൽ പങ്കുവെക്കൽ എന്നാൽ...', ['കുറച്ച് ഭക്ഷണമോ പലഹാരമോ മറ്റുള്ളവർക്ക് കൊടുക്കുക', 'ഒറ്റയ്ക്ക് തിന്നുക', 'മധുരം ഒളിപ്പിക്കുക'], 'പങ്കുവെച്ചാൽ ആഘോഷം കൂടുതൽ സന്തോഷമാകും.'),
 ('A neighbour is ill. What can you do?', ['Ask a grown-up how to help', 'Make a lot of noise', 'Stay away and laugh'], 0, 'A grown-up can show a safe way to help.',
  'ഒരു അയൽക്കാരന് സുഖമില്ല. നിനക്ക് എന്ത് ചെയ്യാം?', ['എങ്ങനെ സഹായിക്കാം എന്ന് വലിയ ഒരാളോട് ചോദിക്കാം', 'ഒരുപാട് ബഹളം ഉണ്ടാക്കാം', 'മാറിനിന്ന് ചിരിക്കാം'], 'സേഫായി സഹായിക്കാനുള്ള വഴി വലിയ ആള് പറഞ്ഞുതരും.'),
 ('Is it okay to share only when you have a lot?', ['No, even a little can help', 'Yes, only then', 'Never share'], 0, 'A small share still helps.',
  'ഒരുപാട് ഉള്ളപ്പോൾ മാത്രം പങ്കുവെച്ചാൽ മതിയോ?', ['വേണ്ട, കുറച്ചായാലും സഹായമാകും', 'മതി, അപ്പോൾ മാത്രം', 'ഒരിക്കലും പങ്കുവെക്കരുത്'], 'കുറച്ചാണെങ്കിലും ഒരു പങ്ക് സഹായമാകും.'),
 ('Giving a gift to a friend with a happy heart is...', ['Kind', 'Unkind', 'Silly'], 0, 'Gifts given happily show love.',
  'സന്തോഷത്തോടെ ഒരു കൂട്ടുകാരന് സമ്മാനം കൊടുക്കുന്നത്...', ['നല്ല കാര്യമാ', 'നല്ലതല്ല', 'മണ്ടത്തരമാ'], 'സന്തോഷത്തോടെ കൊടുക്കുന്ന സമ്മാനം സ്നേഹം കാണിക്കും.'),
 ('Which one is unkind?', ['Not letting anyone play with you', 'Taking turns', 'Saying thank you'], 0, 'Including others is kind.',
  'ഇതിൽ ശരിയല്ലാത്തത് ഏതാ?', ['ആരെയും കൂടെ കളിക്കാൻ സമ്മതിക്കാത്തത്', 'ഊഴം വെച്ച് കളിക്കുന്നത്', 'താങ്ക്സ് പറയുന്നത്'], 'എല്ലാവരെയും കൂടെ കൂട്ടുന്നത് നല്ല കാര്യമാ.'),
 ('Story books you have finished can be...', ['Given to a child who has none', 'Torn up', 'Left in the rain'], 0, 'Passing on books helps others learn.',
  'വായിച്ചു കഴിഞ്ഞ കഥാപ്പുസ്തകങ്ങൾ...', ['പുസ്തകം ഇല്ലാത്ത ഒരു കുട്ടിക്ക് കൊടുക്കാം', 'കീറിക്കളയാം', 'മഴയത്ത് ഇടാം'], 'പുസ്തകം കൈമാറിയാൽ വേറെ കുട്ടികൾക്ക് പഠിക്കാൻ പറ്റും.'),
 ('How do you feel when you help someone?', ['Happy and proud', 'Always tired', 'Angry'], 0, 'Helping feels good.',
  'ഒരാളെ സഹായിക്കുമ്പോൾ നിനക്ക് എന്ത് തോന്നും?', ['സന്തോഷവും അഭിമാനവും', 'എപ്പോഴും ക്ഷീണം', 'ദേഷ്യം'], 'സഹായിക്കുമ്പോൾ മനസ്സിന് സുഖം തോന്നും.'),
],
"s6": [
 ('A candy costs ₹3 and you pay ₹5. What change do you get?', ['₹2', '₹3', '₹8'], 0, '5 minus 3 is 2.',
  'ഒരു മിഠായിക്ക് ₹3 ആണ്, നീ ₹5 കൊടുത്തു. ബാക്കി എത്ര കിട്ടും?', ['₹2', '₹3', '₹8'], '5 ൽ നിന്ന് 3 പോയാൽ 2.'),
 ('An eraser costs ₹4 and you pay ₹10. What change?', ['₹6', '₹4', '₹14'], 0, '10 minus 4 is 6.',
  'ഒരു റബ്ബറിന് ₹4 ആണ്, നീ ₹10 കൊടുത്തു. ബാക്കി എത്ര?', ['₹6', '₹4', '₹14'], '10 ൽ നിന്ന് 4 പോയാൽ 6.'),
 ('A ball costs ₹15 and you pay ₹20. What change?', ['₹5', '₹15', '₹35'], 0, '20 minus 15 is 5.',
  'ഒരു പന്തിന് ₹15 ആണ്, നീ ₹20 കൊടുത്തു. ബാക്കി എത്ര?', ['₹5', '₹15', '₹35'], '20 ൽ നിന്ന് 15 പോയാൽ 5.'),
 ('Two pencils cost ₹3 each. How much for both?', ['₹6', '₹5', '₹33'], 0, '3 plus 3 is 6.',
  'രണ്ട് പെൻസിലിന് ഓരോന്നിനും ₹3 ആണ്. രണ്ടിനും കൂടി എത്ര?', ['₹6', '₹5', '₹33'], '3 ഉം 3 ഉം കൂടിയാൽ 6.'),
 ('A toy costs ₹45 and you pay ₹50. What change?', ['₹5', '₹45', '₹95'], 0, '50 minus 45 is 5.',
  'ഒരു കളിപ്പാട്ടത്തിന് ₹45 ആണ്, നീ ₹50 കൊടുത്തു. ബാക്കി എത്ര?', ['₹5', '₹45', '₹95'], '50 ൽ നിന്ന് 45 പോയാൽ 5.'),
 ('Which price is the highest?', ['₹30', '₹13', '₹3'], 0, '30 is bigger than 13 and 3.',
  'ഏത് വിലയാ ഏറ്റവും കൂടുതൽ?', ['₹30', '₹13', '₹3'], '30 ആണ് 13 നെക്കാളും 3 നെക്കാളും വലുത്.'),
 ('The shopkeeper gives too little change. What do you do?', ['Politely tell them', 'Shout', 'Leave quietly'], 0, 'Speak politely and ask them to check.',
  'കടക്കാരൻ ബാക്കി പൈസ കുറച്ചാ തന്നത്. നീ എന്ത് ചെയ്യും?', ['മര്യാദയ്ക്ക് പറയും', 'ഉറക്കെ ബഹളം വെക്കും', 'മിണ്ടാതെ പോകും'], 'മര്യാദയോടെ പറഞ്ഞ് ഒന്നുകൂടി നോക്കാൻ പറയണം.'),
 ('A ₹10 snack and a ₹5 drink cost...', ['₹15', '₹5', '₹105'], 0, '10 plus 5 is 15.',
  '₹10 ന്റെ ഒരു പലഹാരവും ₹5 ന്റെ ഒരു ജ്യൂസും കൂടി...', ['₹15', '₹5', '₹105'], '10 ഉം 5 ഉം കൂടിയാൽ 15.'),
 ('You pay ₹100 for an ₹80 item. What change?', ['₹20', '₹80', '₹180'], 0, '100 minus 80 is 20.',
  '₹80 ന്റെ സാധനത്തിന് നീ ₹100 കൊടുത്തു. ബാക്കി എത്ര?', ['₹20', '₹80', '₹180'], '100 ൽ നിന്ന് 80 പോയാൽ 20.'),
 ('A bigger number on the price tag means...', ['More money to pay', 'Less money to pay', 'Free'], 0, 'A bigger price means you pay more.',
  'വിലച്ചീട്ടിൽ വലിയ സംഖ്യ ആണെങ്കിൽ...', ['കൂടുതൽ പൈസ കൊടുക്കണം', 'കുറച്ച് പൈസ കൊടുത്താൽ മതി', 'ഫ്രീ ആണ്'], 'വില കൂടിയാൽ നമ്മൾ കൂടുതൽ കൊടുക്കണം.'),
 ('Which one is the cheapest?', ['₹6', '₹16', '₹60'], 0, '6 is the smallest number.',
  'ഏതാ ഏറ്റവും വില കുറഞ്ഞത്?', ['₹6', '₹16', '₹60'], '6 ആണ് ഏറ്റവും ചെറിയ സംഖ്യ.'),
 ('Before paying, we should check...', ['The price', 'The weather', 'The time'], 0, 'Always know how much to pay.',
  'പൈസ കൊടുക്കുന്നതിന് മുൻപ് നമ്മൾ നോക്കേണ്ടത്...', ['വില', 'കാലാവസ്ഥ', 'സമയം'], 'എത്ര കൊടുക്കണം എന്ന് എപ്പോഴും അറിഞ്ഞിരിക്കണം.'),
 ('You have ₹30 and buy a ₹12 book. How much is left?', ['₹18', '₹42', '₹12'], 0, '30 minus 12 is 18.',
  'നിന്റെ കൈയിൽ ₹30 ഉണ്ട്, ₹12 ന്റെ പുസ്തകം വാങ്ങി. എത്ര ബാക്കി?', ['₹18', '₹42', '₹12'], '30 ൽ നിന്ന് 12 പോയാൽ 18.'),
],
"s7": [
 ('A stranger offers sweets and asks you to follow. You...', ['Say no and tell a grown-up', 'Follow them', 'Take the sweets'], 0, 'Never go with strangers.',
  'ഒരു അപരിചിതൻ മധുരം തന്നിട്ട് കൂടെ വരാൻ പറയുന്നു. നീ...', ['വേണ്ട എന്ന് പറഞ്ഞ് വലിയ ഒരാളോട് പറയും', 'കൂടെ പോകും', 'മധുരം വാങ്ങും'], 'അപരിചിതരുടെ കൂടെ ഒരിക്കലും പോകരുത്.'),
 ('Who is allowed to know your secret PIN?', ['Only you, and a trusted parent if needed', 'Anyone who asks', 'A shop assistant'], 0, 'A PIN is a secret.',
  'നിന്റെ രഹസ്യ പിൻ അറിയാൻ ആർക്കാ അനുവാദം?', ['നിനക്കും, വേണമെങ്കിൽ വിശ്വാസമുള്ള അച്ഛനമ്മമാർക്കും മാത്രം', 'ചോദിക്കുന്ന ആർക്കും', 'കടയിലെ ചേട്ടന്'], 'പിൻ ഒരു രഹസ്യമാ.'),
 ('You find a wallet on the road. You...', ['Give it to a grown-up', 'Keep the money', 'Throw it away'], 0, 'A grown-up can find the owner.',
  'വഴിയിൽ നിന്ന് ഒരു പഴ്സ് കിട്ടി. നീ...', ['വലിയ ഒരാളെ ഏൽപ്പിക്കും', 'പൈസ എടുത്ത് വെക്കും', 'വലിച്ചെറിയും'], 'ഉടമസ്ഥനെ കണ്ടുപിടിക്കാൻ വലിയവർക്ക് പറ്റും.'),
 ('A message says: send your OTP to win a prize. You...', ['Do not send it and tell a grown-up', 'Send it', 'Share it with friends'], 0, 'Never share an OTP.',
  '“സമ്മാനം കിട്ടാൻ നിന്റെ ഒടിപി അയക്കൂ” എന്ന് ഒരു മെസ്സേജ്. നീ...', ['അയക്കാതെ വലിയ ഒരാളോട് പറയും', 'അയച്ചുകൊടുക്കും', 'കൂട്ടുകാർക്ക് ഷെയർ ചെയ്യും'], 'ഒടിപി ഒരിക്കലും ആർക്കും കൊടുക്കരുത്.'),
 ('In a crowd, where should you keep your purse?', ['Close and in front of you', 'Open in your hand', 'On the ground'], 0, 'Keep it close so it cannot be taken.',
  'ആൾക്കൂട്ടത്തിൽ നിന്റെ പഴ്സ് എവിടെ വെക്കണം?', ['അടുത്ത്, മുന്നിൽ', 'തുറന്ന് കൈയിൽ', 'നിലത്ത്'], 'ആരും എടുക്കാതിരിക്കാൻ അടുത്ത് തന്നെ വെക്കണം.'),
 ('Telling someone your password is...', ['Unsafe', 'Safe', 'Fun'], 0, 'Passwords are secrets.',
  'നിന്റെ പാസ്\u200cവേഡ് വേറെ ഒരാളോട് പറയുന്നത്...', ['സേഫല്ല', 'സേഫാ', 'രസമാ'], 'പാസ്\u200cവേഡ് ഒരു രഹസ്യമാ.'),
 ('Someone asks to see your savings. You...', ['Say they are private', 'Show them', 'Give them some'], 0, 'Savings are private.',
  'ഒരാൾ നിന്റെ സമ്പാദ്യം കാണണം എന്ന് പറയുന്നു. നീ...', ['അത് പ്രൈവറ്റാണെന്ന് പറയും', 'കാണിച്ചുകൊടുക്കും', 'കുറച്ച് കൊടുക്കും'], 'സമ്പാദ്യം പ്രൈവറ്റാ.'),
 ('After buying something, where do you put the change?', ['Safely in your pocket or bag', 'On the counter', 'On the road'], 0, 'Put it away safely right away.',
  'എന്തെങ്കിലും വാങ്ങിയതിന് ശേഷം ബാക്കി പൈസ എവിടെ വെക്കും?', ['പോക്കറ്റിലോ ബാഗിലോ സേഫായി', 'കൗണ്ടറിൽ', 'റോഡിൽ'], 'ഉടനെ തന്നെ സേഫായി എടുത്തുവെക്കണം.'),
 ('Which is a good place for coins at home?', ['A box or piggy bank', 'Outside in the rain', 'Down the drain'], 0, 'A box keeps them safe and dry.',
  'വീട്ടിൽ നാണയം വെക്കാൻ നല്ല സ്ഥലം ഏതാ?', ['ഒരു പെട്ടിയോ കുടുക്കയോ', 'പുറത്ത് മഴയത്ത്', 'ഓടയിൽ'], 'പെട്ടിയിൽ വെച്ചാൽ സേഫായും നനയാതെയും ഇരിക്കും.'),
 ("A game asks for your parent's card number. You...", ['Ask a parent and do not type it', 'Type it', 'Share it with friends'], 0, 'Card numbers are for grown-ups.',
  'ഒരു ഗെയിം അച്ഛനമ്മമാരുടെ കാർഡ് നമ്പർ ചോദിക്കുന്നു. നീ...', ['അച്ഛനമ്മമാരോട് ചോദിക്കും, ടൈപ്പ് ചെയ്യില്ല', 'ടൈപ്പ് ചെയ്യും', 'കൂട്ടുകാർക്ക് ഷെയർ ചെയ്യും'], 'കാർഡ് നമ്പർ വലിയവർക്ക് മാത്രമുള്ളതാ.'),
 ('Who can help if you lose money?', ['A trusted grown-up', 'A stranger', 'Nobody'], 0, 'Tell a grown-up you trust.',
  'പൈസ കളഞ്ഞുപോയാൽ ആര് സഹായിക്കും?', ['വിശ്വാസമുള്ള ഒരു വലിയ ആൾ', 'ഒരു അപരിചിതൻ', 'ആരും ഇല്ല'], 'നീ വിശ്വസിക്കുന്ന ഒരു വലിയ ആളോട് പറയുക.'),
 ('Locking a cupboard that holds savings keeps them...', ['Safer', 'Lost', 'Wet'], 0, 'A lock helps protect savings.',
  'സമ്പാദ്യം വെച്ച അലമാര പൂട്ടിയാൽ അത്...', ['കൂടുതൽ സേഫാകും', 'കളഞ്ഞുപോകും', 'നനയും'], 'പൂട്ട് ഉണ്ടെങ്കിൽ സമ്പാദ്യം കൂടുതൽ സേഫാണ്.'),
 ('Being honest about a money mistake is...', ['Good', 'Bad', 'Silly'], 0, 'Honesty helps fix mistakes.',
  'പൈസയിൽ പറ്റിയ ഒരു തെറ്റിനെ കുറിച്ച് സത്യം പറയുന്നത്...', ['നല്ല കാര്യമാ', 'മോശം കാര്യമാ', 'മണ്ടത്തരമാ'], 'സത്യം പറഞ്ഞാൽ തെറ്റ് തിരുത്താൻ എളുപ്പമാകും.'),
],
}
'''

_SOURCES['more_data'] = r'''"""Collects the extra questions (English and Malayalam side by side) from the more_data_* files."""
import importlib

DATA = {}
for _name in ("more_data_seed", "more_data_explore", "more_data_pioneer"):
    try:
        DATA.update(importlib.import_module(_name).DATA)
    except ImportError:
        pass
'''

_SOURCES['content'] = r'''"""EasyFin content (powered by NYZTrade): 3 age bands, 22 lessons, 264 quiz questions.

Each lesson has: a 3 part story, one game (activity) and a bank of 12 quiz
questions. A play draws 5 random questions from the bank, so replays differ.
Quick Quiz mode mixes questions from every lesson in an age band.

A question is a tuple: (question, [options], index_of_right_option, why).
Options are shuffled when shown. All figures are examples for teaching, not
advice. Nothing here recommends buying any product.
"""

QUESTIONS_PER_PLAY = 5
QUICK_QUIZ_LENGTH = 10

BANDS = [
    {"id": "seed", "name": "Seedlings", "ages": "Ages 5 to 7", "note": "Pictures, sounds and tiny steps"},
    {"id": "explore", "name": "Explorers", "ages": "Ages 8 to 10", "note": "Habits, profit and staying safe"},
    {"id": "pioneer", "name": "Pioneers", "ages": "Ages 11 to 14", "note": "Growth, risk and the real world"},
]

# ----------------------------------------------------------------- Seedlings
S1 = [
    ("Which is worth the most?", ["₹2 coin", "₹5 coin", "₹10 note"], 2, "10 is bigger than 5 and 2."),
    ("How many ₹1 coins make ₹5?", ["2", "5", "10"], 1, "Five ones make five."),
    ("You pay ₹10 for a ₹3 toffee. How much does the shopkeeper give back?", ["₹3", "₹7", "₹10"], 1, "10 minus 3 is 7."),
    ("Which number is the biggest?", ["₹5", "₹20", "₹10"], 1, "20 is more than 10 and 5."),
    ("Where is a safe place to keep your money?", ["In a piggy bank at home", "On a bus seat", "With a stranger"], 0, "A piggy bank at home keeps it safe."),
    ("What do we give the shopkeeper to buy a biscuit?", ["Money", "Leaves", "Stones"], 0, "Shops accept money."),
    ("Two ₹5 coins make how much?", ["₹7", "₹10", "₹52"], 1, "5 plus 5 is 10."),
    ("Which one is made of paper?", ["A note", "A coin", "A key"], 0, "Notes are paper money."),
    ("₹5 + ₹5 + ₹1 = ?", ["₹10", "₹11", "₹55"], 1, "10 plus 1 is 11."),
    ("A pencil costs ₹6. You have ₹5. What do you need?", ["₹1 more", "₹5 more", "Nothing"], 0, "6 minus 5 is 1."),
    ("Which shows the most money?", ["Three ₹1 coins", "One ₹5 coin", "Two ₹1 coins"], 1, "5 is more than 3 or 2."),
    ("You find a coin on the road. What should you do?", ["Tell a grown-up", "Throw it away", "Hide it"], 0, "A grown-up can help."),
]
S2 = [
    ("Which one is a need?", ["Chocolate", "Warm food", "Toy robot"], 1, "Food keeps us healthy."),
    ("You want a new toy, but you also need school books. What comes first?", ["The toy", "The school books", "Both, always"], 1, "Needs come first. The toy can wait."),
    ("Is it wrong to buy things we want?", ["Yes, never", "No, once needs are done and we have saved for it", "Only on Sundays"], 1, "Wants are fine when we plan for them."),
    ("Which one is a want?", ["Water", "Medicine", "Video game"], 2, "We can live without a video game."),
    ("Which do we need every day to live?", ["Food and water", "Balloons", "Stickers"], 0, "Food and water keep our body working."),
    ("Ice cream is a...", ["Need", "Want", "Medicine"], 1, "It is a nice treat."),
    ("School books and a school bag are...", ["Needs for learning", "Only wants", "Not useful"], 0, "They help us learn."),
    ("Before buying a want, what should we check?", ["That we have money left after our needs", "That friends have one", "That it is on sale"], 0, "Needs are paid first."),
    ("Medicine when we are sick is a...", ["Need", "Want", "Toy"], 0, "It helps us get better."),
    ("A toy car is a...", ["Need", "Want", "Food"], 1, "Toys are fun but not a must."),
    ("Which pair has two needs?", ["Food and water", "Toy and candy", "Game and balloon"], 0, "Both keep us alive and healthy."),
    ("Money is short. What do we buy first?", ["Rice for dinner", "A sticker", "A toy"], 0, "Food is a need."),
]
S3 = [
    ("Pinku saves ₹5 every day. How many days to save ₹30?", ["4 days", "6 days", "10 days"], 1, "5 times 6 is 30."),
    ("Meera buys sweets every day. Pinku saves. Who gets the toy cycle first?", ["Meera", "Pinku", "The same day"], 1, "Saving moves you closer to the goal."),
    ("Saving means...", ["Spending it all today", "Keeping some money for later", "Hiding it from everyone"], 1, "We keep some for later."),
    ("Where is a good place to keep your savings?", ["A piggy bank at home", "Your open pocket", "With a stranger"], 0, "A piggy bank at home keeps it safe."),
    ("You save ₹2 each day for 5 days. How much do you have?", ["₹7", "₹10", "₹25"], 1, "2 times 5 is 10."),
    ("What helps you reach a big goal?", ["Patience", "Spending quickly", "Losing coins"], 0, "Small steps over time reach the goal."),
    ("Your piggy bank has ₹20. The toy costs ₹50. How much more do you need?", ["₹20", "₹30", "₹70"], 1, "50 minus 20 is 30."),
    ("Many small coins together can become...", ["A lot of money", "Nothing", "Less money"], 0, "Small amounts add up."),
    ("You save ₹10 every week. How much after 4 weeks?", ["₹14", "₹40", "₹100"], 1, "10 times 4 is 40."),
    ("When is a good time to start saving?", ["Today", "Never", "When we are old"], 0, "Starting early builds the habit."),
    ("Which one is saving?", ["Putting ₹5 in the piggy bank", "Buying candy", "Losing a coin"], 0, "Saving means keeping the money."),
    ("A friend asks for all your savings. What do you do?", ["Ask a trusted grown-up first", "Give it all", "Hide it"], 0, "Big money decisions are made with a grown-up."),
]
S4 = [
    ("Where does money usually come from?", ["Work", "Trees", "Wishing"], 0, "People earn money by working."),
    ("A farmer sells vegetables. What is that?", ["Earning money", "A gift", "Losing money"], 0, "Selling what you grow is earning."),
    ("What is a gift of money?", ["Money given with love, not for work", "Money from a shop", "Money we find"], 0, "Gifts are given freely."),
    ("A teacher teaches students. How do they earn?", ["They get a salary", "They sell toys", "They find coins"], 0, "A salary is pay for work."),
    ("Vishu Kaineettam is...", ["Gift money from elders", "Pay for a job", "A bank loan"], 0, "Elders give it as a blessing."),
    ("How can a young person earn a little in a fair, safe way?", ["Selling homemade cards to neighbours", "Taking money from a bag", "Asking strangers for money"], 0, "Making and selling is honest work."),
    ("How do doctors earn money?", ["By treating sick people", "By selling sweets", "By driving buses"], 0, "Their work is helping patients."),
    ("Why do people work?", ["To earn money for food and needs", "Only to be tired", "To lose money"], 0, "Work pays for the things we need."),
    ("You sell 2 pencils at ₹5 each. How much do you get?", ["₹7", "₹10", "₹25"], 1, "5 times 2 is 10."),
    ("A bus driver earns money by...", ["Driving people to places", "Reading books", "Planting trees"], 0, "Passengers pay for the ride."),
    ("Helping at home is...", ["Something we do because we care", "Always paid", "Not allowed"], 0, "Family members help each other."),
    ("Why does a shopkeeper charge money for biscuits?", ["They pay for the goods and earn a living", "To trick us", "Biscuits are rare"], 0, "Shopkeepers buy goods and earn from sales."),
]
S5 = [
    ("Sharing means...", ["Giving some of what you have to help others", "Keeping everything", "Hiding things"], 0, "Sharing is helping."),
    ("A friend has no lunch. What can you do?", ["Share some of yours", "Laugh at them", "Hide your lunch"], 0, "Sharing food is kind."),
    ("Which is a kind use of money?", ["Helping someone in need", "Throwing coins away", "Hiding coins forever"], 0, "Kind money helps people."),
    ("A charity box collects money to...", ["Help others", "Buy candy for ourselves", "Pay the bus"], 0, "Charity helps people in need."),
    ("Is a small gift still helpful?", ["Yes, small help matters", "No, only big gifts count", "Only on festivals"], 0, "Little acts add up."),
    ("Which is not kind?", ["Laughing at a friend with no money", "Sharing pencils", "Giving old clothes"], 0, "We never tease others."),
    ("You outgrew your clothes. What can you do?", ["Give them to someone who needs them", "Throw them on the road", "Hide them"], 0, "Passing things on helps others."),
    ("How does sharing often make us feel?", ["Happy", "Always sad", "Angry"], 0, "Kindness feels good."),
    ("You have 2 laddus and a friend has none. What can you do?", ["Share one", "Eat both fast", "Hide them"], 0, "Sharing is kind."),
    ("Who can you help with money or things?", ["Family, friends and neighbours", "Nobody", "Only strangers online"], 0, "Help people you know and trust."),
    ("The Share jar is for...", ["Helping others", "Only toys", "Losing coins"], 0, "It is money set aside to give."),
    ("True or false: only rich people can share.", ["False, anyone can share", "True", "Only adults"], 0, "Anyone can share something."),
]
S6 = [
    ("A toffee costs ₹2. You give ₹5. What change do you get?", ["₹2", "₹3", "₹5"], 1, "5 minus 2 is 3."),
    ("A banana costs ₹5. You give ₹10. What change do you get?", ["₹5", "₹10", "₹15"], 0, "10 minus 5 is 5."),
    ("A pencil costs ₹7. You give ₹10. What change?", ["₹3", "₹7", "₹17"], 0, "10 minus 7 is 3."),
    ("Which costs less?", ["₹5", "₹8", "₹10"], 0, "5 is the smallest number."),
    ("You have ₹20 and buy a ₹15 book. How much is left?", ["₹5", "₹15", "₹35"], 0, "20 minus 15 is 5."),
    ("The shopkeeper says ₹12. Which money pays exactly?", ["₹10 and ₹2", "₹5 and ₹5", "₹2 and ₹1"], 0, "10 plus 2 is 12."),
    ("Why should we check our change?", ["To be sure it is right", "It is a rule for kids only", "No reason"], 0, "Everyone checks change."),
    ("Which costs the most?", ["₹9", "₹15", "₹50"], 2, "50 is the biggest."),
    ("Two biscuits cost ₹5 each. How much for both?", ["₹5", "₹10", "₹25"], 1, "5 plus 5 is 10."),
    ("You have ₹10. A toy costs ₹12. What can you do?", ["Save ₹2 more", "Take it anyway", "Ask for it free"], 0, "Saving a little more gets it."),
    ("A price tag tells us...", ["How much something costs", "Who made it", "How heavy it is"], 0, "The price is what we pay."),
    ("You give ₹20 for a ₹20 notebook. What change?", ["₹0, no change", "₹20", "₹40"], 0, "Exact money means no change."),
]
S7 = [
    ("Where is a safe place for savings?", ["At home with a trusted grown-up", "On a bus seat", "With a stranger"], 0, "Keep savings with people you trust."),
    ("A stranger offers you money to come with them. What do you do?", ["Say no and tell a grown-up", "Go with them", "Take the money"], 0, "Never go with strangers."),
    ("Who can know your secret PIN?", ["Only you, and your parent if needed", "All your friends", "Everyone"], 0, "PINs are secret."),
    ("You find money on the road. What do you do?", ["Tell a grown-up", "Hide it", "Throw it away"], 0, "A grown-up can help find the owner."),
    ("Should you show all your savings to strangers?", ["No", "Yes", "Only on Sundays"], 0, "Keep savings private."),
    ("Before buying something online, you should...", ["Ask a parent", "Click quickly", "Share the PIN"], 0, "Online buying needs a grown-up."),
    ("After a shop gives you change, you should...", ["Count it before you leave", "Run away", "Throw it"], 0, "Count so nothing is missing."),
    ("Who should hold big amounts of money?", ["A grown-up you trust", "A new friend online", "Nobody"], 0, "Big money stays with trusted adults."),
    ("A message says you won a prize. What now?", ["Show a grown-up", "Click the link", "Reply with your address"], 0, "Prize messages are often tricks."),
    ("Your friend asks for your parent's phone PIN. You say...", ["No, it is a secret", "Yes", "Maybe"], 0, "Never share PINs."),
    ("If you lose money, you should...", ["Tell a grown-up honestly", "Hide it", "Blame a friend"], 0, "Telling the truth helps solve it."),
    ("Is a piggy bank at home a good place for coins?", ["Yes", "No, a rooftop is better", "No, give them to strangers"], 0, "It is safe and easy to count."),
]

# ----------------------------------------------------------------- Explorers
E1 = [
    ("You get ₹200 and save a quarter of it. How much do you save?", ["₹25", "₹50", "₹100"], 1, "A quarter of 200 is 50."),
    ("What is the Share jar for?", ["Helping others or giving gifts", "Buying more toys", "Hiding money"], 0, "Sharing helps people around us."),
    ("When is the best time to decide your split?", ["After spending everything", "Before you start spending", "Never"], 1, "A plan made first protects your savings."),
    ("You get ₹100 and save 20%. How much do you save?", ["₹10", "₹20", "₹80"], 1, "20% of 100 is 20."),
    ("Which jar helps you buy bigger things later?", ["Save", "Spend", "Neither"], 0, "Savings grow into bigger goals."),
    ("Your Spend jar is empty before month end. What is best?", ["Wait for next month", "Take from the Save jar", "Borrow from a friend"], 0, "Stick to your plan and wait."),
    ("Half of ₹200 is...", ["₹50", "₹100", "₹150"], 1, "200 divided by 2 is 100."),
    ("Why use three jars?", ["To plan money for different uses", "To confuse people", "To lose money"], 0, "Jars give every rupee a job."),
    ("A friend wants you to spend it all on a game. What is smart?", ["Stick to your plan", "Spend it all", "Share it all"], 0, "Plans beat impulse."),
    ("Which is a good habit with money?", ["Save first, then spend", "Spend first, save what is left", "Never save"], 0, "Saving first makes sure it happens."),
    ("You split ₹200 as ₹100, ₹70 and ₹30. Which total is right?", ["₹200", "₹170", "₹230"], 0, "100 plus 70 plus 30 is 200."),
    ("Sharing a little each month teaches you to...", ["Care about others", "Waste money", "Stop saving"], 0, "Giving builds kindness."),
]
E2 = [
    ("What is profit?", ["Sales plus costs", "Sales minus costs", "Only the price"], 1, "Profit is what is left after costs."),
    ("A glass costs ₹6 to make and sells for ₹4. What happens?", ["Profit of ₹2", "Loss of ₹2 on each glass", "No change"], 1, "You get 4 but spend 6, so you lose 2."),
    ("What usually happens when the price goes up a lot?", ["More people buy", "Fewer people buy", "Nothing"], 1, "High prices put customers off."),
    ("You sell 10 glasses at ₹15. How much money comes in?", ["₹25", "₹150", "₹1,500"], 1, "10 times 15 is 150."),
    ("Each glass costs ₹6 and you make 10. What are your costs?", ["₹16", "₹60", "₹600"], 1, "6 times 10 is 60."),
    ("Sales are ₹150 and costs are ₹60. What is the profit?", ["₹210", "₹90", "₹60"], 1, "150 minus 60 is 90."),
    ("If lemons cost more, your costs...", ["Go up", "Go down", "Stay zero"], 0, "Higher ingredient prices mean higher costs."),
    ("Selling below cost means you...", ["Lose money", "Make more profit", "Break even"], 0, "Each sale loses money."),
    ("Break even means...", ["Sales equal costs, no profit and no loss", "Huge profit", "Giving things away free"], 0, "You neither gain nor lose."),
    ("On a rainy day, fewer people want cold drinks. What should you expect?", ["Lower sales", "Higher sales", "The same sales"], 0, "Weather changes demand."),
    ("Is the highest price always the best?", ["No, too high a price can cut sales", "Yes, always", "Only on Sundays"], 0, "Find a balance."),
    ("Which helps a stall do well?", ["A fair price and good quality", "Rude service", "Hiding the price"], 0, "Happy customers come back."),
]
E3 = [
    ("Who is allowed to ask for your UPI PIN?", ["The bank", "Nobody", "A teacher"], 1, "A PIN is yours alone."),
    ("A stranger online offers a gift if you share an OTP. What do you do?", ["Share it quickly", "Do not share, and tell a trusted adult", "Ask for two gifts"], 1, "OTPs are never shared."),
    ("Which is the safest way to pay at a shop?", ["Pay with a parent beside you", "Send money to someone who messaged you", "Share your PIN so it is faster"], 0, "Pay with a trusted adult at a real shop."),
    ("A link says you won a phone. What should you do?", ["Click to claim it", "Ignore it and show a grown-up", "Share it with friends"], 1, "Free prizes that need a click are usually tricks."),
    ("A caller says they are from the bank and need your OTP. What is true?", ["Banks never ask for your OTP", "Banks always ask for it", "Only on Mondays"], 0, "Never share an OTP with anyone."),
    ("To receive money by UPI, do you enter your PIN?", ["No, never", "Yes, always", "Only for big amounts"], 0, "A PIN is only for sending money."),
    ("Which message looks like a scam?", ["Urgent! Your account closes in 1 hour, click here", "Your parent says dinner is ready", "Your teacher says homework is due Friday"], 0, "Scams use panic and hurry."),
    ("A game chat friend asks for your parent's card number. You...", ["Say no and tell a parent", "Send it", "Send half"], 0, "Never share card details."),
    ("If you think you were tricked, you should...", ["Tell a trusted adult quickly", "Hide it", "Do nothing"], 0, "Fast reporting limits damage."),
    ("Is a screenshot of 'payment done' always proof of payment?", ["No, check your bank or app message", "Yes, always", "Only if it is blurry"], 0, "Fake screenshots exist."),
    ("A stranger sends a request to 'collect' money from you. You should...", ["Decline it", "Enter your PIN to accept", "Share the OTP"], 0, "Approving a collect request sends your money."),
    ("Which makes a strong password?", ["A long mix of letters, numbers and symbols", "1234", "Your birthday"], 0, "Hard-to-guess passwords are safer."),
]
E4 = [
    ("What is a budget?", ["A plan for how to use money", "A kind of shop", "A bank card"], 0, "A budget tells your money where to go."),
    ("What should a budget cover first?", ["Needs", "Wants", "Treats"], 0, "Needs come first."),
    ("You have ₹400 and plan ₹100 for savings. What share is that?", ["10%", "25%", "50%"], 1, "100 is a quarter of 400."),
    ("What is overspending?", ["Spending more than you planned or have", "Saving too much", "Counting coins"], 0, "Spending beyond the budget causes trouble."),
    ("Why track your spending?", ["To see where money goes", "To spend more", "To hide it"], 0, "Tracking shows patterns."),
    ("A new game costs more than your Fun money. What is smart?", ["Wait and save for it", "Take from School money", "Borrow secretly"], 0, "Do not take from your needs."),
    ("An emergency fund is...", ["Money kept for surprises", "Money for toys", "Money to lend to friends"], 0, "It protects you from sudden costs."),
    ("Your monthly money is ₹300 and you spend ₹120 on snacks. What is left?", ["₹120", "₹180", "₹420"], 1, "300 minus 120 is 180."),
    ("Which is a good budget habit?", ["Write down money in and money out", "Guess everything", "Never look"], 0, "Writing keeps you honest."),
    ("You plan ₹50 savings a month. How much in 6 months?", ["₹56", "₹300", "₹3,000"], 1, "50 times 6 is 300."),
    ("Money runs out early in the month. What should you do?", ["Adjust next month's plan", "Ignore it", "Spend more"], 0, "Learn from it and improve."),
    ("What is the first step of making a budget?", ["Know how much money you have", "Buy something", "Ask a friend"], 0, "Start with money coming in."),
]
E5 = [
    ("What is a bank?", ["A place that keeps money safe and lends money", "A shop for toys", "A playground"], 0, "Banks keep and lend money."),
    ("What is interest on savings?", ["Extra money the bank pays you for keeping money there", "A fee for losing a card", "A type of coin"], 0, "Interest rewards savers."),
    ("Why is a bank safer than under the bed?", ["Banks protect money with security", "Banks hide it from you", "It is not safer"], 0, "Banks have locks, guards and records."),
    ("Putting money in a bank is called...", ["Deposit", "Withdraw", "Borrow"], 0, "Deposit means putting in."),
    ("Taking money out of an account is called...", ["Withdraw", "Deposit", "Interest"], 0, "Withdraw means taking out."),
    ("Who helps a child open a savings account?", ["A parent or guardian", "A stranger", "Nobody"], 0, "Children need a guardian's help."),
    ("A passbook or statement shows...", ["Money in and money out", "The weather", "Your marks"], 0, "It records your transactions."),
    ("When you borrow from a bank, you usually pay back...", ["The money plus interest", "Less than you borrowed", "Nothing"], 0, "Interest is the price of borrowing."),
    ("Which is a safe way to check your balance?", ["The bank's official app or branch, with a parent", "A random link in a message", "A stranger's phone"], 0, "Use official channels only."),
    ("An ATM card is used to...", ["Take out money from your account at a machine", "Play games", "Open a shop"], 0, "Cards need PINs kept secret."),
    ("A bank account earns more interest when you...", ["Leave money there for longer", "Spend it daily", "Share your PIN"], 0, "Time helps savings grow."),
    ("What should you never share about your bank account?", ["PIN, OTP and password", "Your favourite colour", "Your pet's name"], 0, "Secrets protect your money."),
]
E6 = [
    ("UPI stands for...", ["Unified Payments Interface", "Ultra Phone Internet", "Universal Paper Income"], 0, "UPI lets banks connect for quick payments."),
    ("When must a UPI PIN be entered?", ["Only when sending money", "When receiving money", "Never"], 0, "Receiving money never needs a PIN."),
    ("What does a QR code do at a shop?", ["Holds the shop's payment details", "Prints a bill", "Opens the door"], 0, "Scanning shows who you pay."),
    ("Before paying, you should check...", ["The name and amount", "The colour of the phone", "The weather"], 0, "Make sure it is the right shop and amount."),
    ("Who enters the PIN when you pay with a parent's phone?", ["The parent", "The shopkeeper", "A friend"], 0, "PINs stay private."),
    ("A message says 'Pay ₹1 to claim ₹5,000'. This is...", ["A scam", "Safe", "A bank rule"], 0, "Real prizes do not ask for money first."),
    ("What proves a payment worked?", ["The success message in your app", "A friend's word", "A screenshot alone"], 0, "Check the app."),
    ("Is it safe to use public Wi-Fi for payments?", ["It is risky, so use mobile data or trusted Wi-Fi", "Always safe", "Only at night"], 0, "Public networks can be watched."),
    ("A wrong UPI ID was typed. What may happen?", ["Money goes to the wrong person", "Nothing at all", "Money doubles"], 0, "Check IDs carefully."),
    ("Why lock your phone?", ["So others cannot use your apps", "To save battery", "To hide games"], 0, "A lock protects payment apps."),
    ("Should kids use UPI alone?", ["Use it with a parent's help", "Yes, alone, always", "Share the PIN with friends"], 0, "A trusted adult should supervise."),
    ("What should you do if you pay by mistake?", ["Tell a parent and contact the bank or app support", "Pay again", "Ignore it"], 0, "Report quickly through official channels."),
]
E7 = [
    ("A good goal says what, how much and by when. Which is best?", ["I want a football costing ₹500 in 10 weeks", "I want something someday", "I want money"], 0, "Clear goals are easier to reach."),
    ("A goal costs ₹600. You save ₹100 a month. How many months?", ["3", "6", "60"], 1, "600 divided by 100 is 6."),
    ("You save ₹50 a week. How much in 4 weeks?", ["₹54", "₹200", "₹500"], 1, "50 times 4 is 200."),
    ("Breaking a big goal into small steps makes it...", ["Easier", "Harder", "Impossible"], 0, "Small steps feel doable."),
    ("Which is better for a long goal?", ["Save a little regularly", "Wait and hope", "Spend it and borrow"], 0, "Regular saving works."),
    ("You have ₹200 and the goal is ₹500. How much more?", ["₹200", "₹300", "₹700"], 1, "500 minus 200 is 300."),
    ("A friend buys sweets daily. What keeps you on track?", ["Remember your goal", "Copy them", "Quit saving"], 0, "Goals give you a reason."),
    ("Tracking your savings on a chart helps because...", ["You can see progress", "It costs money", "It slows you down"], 0, "Seeing progress keeps you going."),
    ("A dream costs a lot. What can you do?", ["Plan, save and be patient", "Give up at once", "Take without asking"], 0, "Patience and planning make dreams real."),
    ("A goal to buy a toy is a...", ["Want, planned for", "Need", "Medicine"], 0, "Wants are fine when planned."),
    ("You reach your goal early. What can you do?", ["Celebrate and set a new goal", "Hide the money", "Never save again"], 0, "Keep the habit going."),
    ("What can make a goal take longer?", ["Spending the saved money", "Saving more", "Counting coins"], 0, "Spending slows you down."),
]

# ----------------------------------------------------------------- Pioneers
P1 = [
    ("₹1,000 grows at 10% a year with compounding. What is it after 2 years?", ["₹1,200", "₹1,210", "₹1,100"], 1, "It becomes 1,100 after year one, then 10% of 1,100 adds 110."),
    ("What helps compounding the most?", ["Starting early and staying invested", "Waiting until you are older", "Spending the interest right away"], 0, "More time means more growth on growth."),
    ("Interest earned on past interest is called...", ["Simple interest", "Compound interest", "Pocket money"], 1, "That is the definition of compounding."),
    ("₹100 grows 10% a year for 3 years with compounding. About how much?", ["₹130", "₹133", "₹300"], 1, "100 times 1.1 three times is 133.1."),
    ("The Rule of 72 says money doubles in about 72 divided by the yearly rate. At 8%, how many years?", ["About 9", "About 18", "About 72"], 0, "72 divided by 8 is 9."),
    ("Which grows more at the same rate: ₹1,000 for 10 years or for 20 years?", ["20 years", "10 years", "They are the same"], 0, "Time is the key ingredient."),
    ("Simple interest is paid on...", ["The original amount only", "Interest only", "Nothing"], 0, "Compound interest also earns on past interest."),
    ("Why do people say 'start early'?", ["Money has more time to grow", "Banks open early", "It is a law"], 0, "Early money compounds for longer."),
    ("If growth is 0%, compounding...", ["Does nothing", "Doubles money", "Triples money"], 0, "No growth means nothing to compound."),
    ("Regular monthly saving plus compounding is useful because...", ["Each deposit starts growing", "Banks forget it", "It avoids all risk"], 0, "Small regular amounts add up over time."),
    ("A growth rate shown in a game is...", ["An example, not a promise", "Guaranteed", "Illegal"], 0, "Real returns vary."),
    ("What happens if you take out your interest every year?", ["There is less compounding", "There is more compounding", "Tax vanishes"], 0, "Leaving it in lets it grow too."),
]
P2 = [
    ("Why do investors spread money across different things?", ["To reduce the chance of one big loss", "To pay more tax", "Because it is a rule"], 0, "If one thing falls, others may hold up."),
    ("A share is...", ["A loan to a friend", "A small piece of ownership in a company", "A type of coin"], 1, "Share owners own a small part of the company."),
    ("A chance of high returns usually comes with...", ["Higher risk", "No risk", "Guaranteed profit"], 0, "Bigger possible gains usually mean bigger possible losses. Nothing is guaranteed."),
    ("NSE and BSE are...", ["Stock exchanges in India", "Banks", "Schools"], 0, "They are places where shares are traded."),
    ("What is diversification?", ["Not putting all your money in one place", "Spending it all", "Buying only one share"], 0, "Spreading reduces risk."),
    ("Sensex and Nifty are...", ["Indexes that track a group of big companies", "Names of banks", "Coins"], 0, "They show how the market moves overall."),
    ("Share prices move because...", ["Buyers and sellers change their minds", "A teacher decides", "They never move"], 0, "Demand and news move prices."),
    ("Money needed soon, like next month's fees, should...", ["Not be put in risky investments", "Be put into shares", "Be lent to strangers"], 0, "Short-term needs call for safe money."),
    ("Who regulates the securities market in India?", ["SEBI", "The school board", "The postal service"], 0, "SEBI protects investors."),
    ("A dividend is...", ["A share of a company's profit paid to shareholders", "A fine", "A kind of loan"], 0, "Some companies share profits."),
    ("Who operates an investment account for a child in India?", ["A parent or guardian", "The child alone", "A stranger"], 0, "Guardians run accounts for minors."),
    ("Which statement is true?", ["Past performance does not guarantee future results", "Shares never fall", "Everyone gets rich fast"], 0, "Prices can go down as well as up."),
]
P3 = [
    ("Prices rise 6% a year. A ₹100 snack costs how much after 1 year?", ["₹94", "₹106", "₹160"], 1, "6% of 100 is 6, so the price is 106."),
    ("What is inflation?", ["Prices rising over time", "Money getting heavier", "Banks closing"], 0, "Inflation is a general rise in prices."),
    ("Cash kept in a cupboard for 10 years will probably...", ["Buy more than today", "Buy less than today", "Buy exactly the same"], 1, "Prices rise, so the same cash buys less."),
    ("A bank pays 4% and prices rise 6%. Your buying power...", ["Falls", "Rises", "Stays exactly the same"], 0, "Prices grew faster than your savings."),
    ("A ₹100 snack at 10% yearly inflation costs how much after 2 years?", ["₹110", "₹120", "₹121"], 2, "100 times 1.1 times 1.1 is 121."),
    ("Why do grandparents say things were cheaper?", ["Inflation raised prices over time", "Shops lied", "Money got smaller on paper"], 0, "Prices rose through the years."),
    ("To beat inflation, savings need to grow...", ["Faster than prices rise", "Slower than prices", "Never"], 0, "Growth must outpace inflation."),
    ("Which usually gets more expensive over many years?", ["Movie tickets and school fees", "Nothing", "Air"], 0, "Most prices drift upward."),
    ("Pocket money stays the same while prices rise. You can buy...", ["Less", "More", "The same"], 0, "Buying power drops."),
    ("Lower inflation means prices rise...", ["More slowly", "Faster", "Never again"], 0, "Prices still rise, only slower."),
    ("Which can help protect money against inflation over the long term?", ["Investing wisely for growth", "Hiding cash", "Spending everything now"], 0, "Money needs to grow to keep up. Nothing is guaranteed."),
    ("Deflation is...", ["Prices falling", "Prices rising", "No money"], 0, "It is the opposite of inflation."),
]
P4 = [
    ("What is a fixed deposit (FD)?", ["Money kept with a bank for a fixed time at a set interest", "A share in a company", "A loan from a friend"], 0, "FDs offer predictable interest."),
    ("A mutual fund...", ["Pools money from many people and invests it", "Is a guaranteed gift", "Is only for banks"], 0, "A fund manager invests the pooled money."),
    ("Which usually has the most predictable return?", ["A bank fixed deposit", "A single share", "A lottery ticket"], 0, "FD rates are fixed in advance."),
    ("Which is more likely to swing up and down?", ["A single company's share", "A passbook", "A piggy bank"], 0, "Shares are volatile."),
    ("Gold prices...", ["Go up and down over time", "Never change", "Always rise"], 0, "No investment is certain."),
    ("Why do people hold more than one kind of investment?", ["To spread risk", "To confuse tax officers", "Because FDs are illegal"], 0, "A mix reduces risk."),
    ("Who manages a mutual fund?", ["A professional fund manager", "The child", "Random people"], 0, "Managers pick the investments."),
    ("'Past returns do not guarantee future returns' means...", ["The future can be different", "The past always repeats", "Funds are illegal"], 0, "Always remember risk."),
    ("Which one is like lending money to a bank?", ["A fixed deposit", "A share", "A gold coin"], 0, "Banks pay interest for using your money."),
    ("Which gives part ownership in a business?", ["A share", "An FD", "A passbook"], 0, "Shareholders are part owners."),
    ("Which statement is true?", ["All investing carries some risk", "FDs never end", "Gold always rises"], 0, "Understand risk before investing."),
    ("Before investing, what should you do?", ["Learn, set goals and talk to a trusted adult", "Follow tips from strangers online", "Borrow to invest"], 0, "Never invest on tips or borrowed money."),
]
P5 = [
    ("When you borrow money, you usually pay back...", ["The amount plus interest", "Less than you borrowed", "Nothing"], 0, "Interest is the cost of borrowing."),
    ("EMI stands for...", ["Equated Monthly Instalment", "Easy Money Idea", "Extra Money Income"], 0, "It is a fixed amount paid each month."),
    ("A higher interest rate means you pay...", ["More in total", "Less in total", "The same"], 0, "Higher rates cost more."),
    ("A longer loan period usually means...", ["Smaller monthly payments but more total interest", "Less total interest", "No interest"], 0, "Time adds interest."),
    ("Paying only the minimum on a credit card bill...", ["Keeps interest charges growing", "Clears the debt fast", "Gives you a gift"], 0, "Unpaid balances charge interest."),
    ("Which loan can be useful?", ["A planned loan for education", "A loan to buy things you want on impulse", "A loan from a stranger's app"], 0, "Borrow for needs, with a plan."),
    ("A credit score shows...", ["How reliably you repay loans", "How tall you are", "Your school marks"], 0, "Lenders use it to judge risk."),
    ("Who should you borrow from?", ["Trusted, regulated lenders", "Unknown loan apps", "Strangers online"], 0, "Use regulated lenders."),
    ("A loan app asks for your phone contacts and photos. You should...", ["Be careful and avoid it", "Allow everything", "Share it with friends"], 0, "Unsafe apps misuse data."),
    ("Before taking a loan, you should check...", ["Interest rate, fees and repayment time", "The colour of the form", "Only the first month"], 0, "Know the full cost."),
    ("A debt trap happens when...", ["You keep borrowing to repay old loans", "You save every month", "You pay on time"], 0, "It is hard to escape."),
    ("Which is a better choice if you can wait?", ["Save up and buy later", "Borrow at high interest", "Skip your needs"], 0, "Waiting avoids interest."),
]
P6 = [
    ("GST is...", ["A tax on goods and services", "A type of bank", "A school fee"], 0, "GST stands for Goods and Services Tax."),
    ("Why do governments collect taxes?", ["To fund roads, schools and hospitals", "To buy sweets", "To close shops"], 0, "Taxes pay for public services."),
    ("Gross salary is...", ["Salary before deductions", "Salary after tax", "Bonus only"], 0, "Net salary is what remains."),
    ("Net salary or take-home pay is...", ["What you receive after deductions", "Salary before deductions", "The tax paid"], 0, "It is the amount that reaches you."),
    ("A payslip shows...", ["Earnings and deductions", "The weather", "School marks"], 0, "It explains how pay is calculated."),
    ("PAN stands for...", ["Permanent Account Number", "Public Asset Note", "Paid Amount Number"], 0, "It identifies taxpayers."),
    ("TDS means...", ["Tax deducted at source", "Tax due on Sunday", "Total daily sales"], 0, "Tax may be deducted before you receive pay."),
    ("Income tax is paid on...", ["Income above certain limits", "Every coin you find", "Only gifts of love"], 0, "Rules set the limits and rates."),
    ("What does an income tax return do?", ["Reports your income and tax to the government", "Buys a house", "Opens a bank"], 0, "It is an annual report."),
    ("A bill with GST shows...", ["Tax added to the price", "The shop's address only", "Nothing extra"], 0, "GST is part of what you pay."),
    ("Which is a good habit with a first salary?", ["Plan: needs, savings, then wants", "Spend it all in a day", "Lend it to strangers"], 0, "Plan the money."),
    ("Who must pay taxes?", ["People and businesses as the law requires", "Only children", "Nobody"], 0, "Everyone follows the rules for their situation."),
]
P7 = [
    ("Profit margin is...", ["Profit as a share of the selling price", "The shop's rent", "A discount"], 0, "It shows how much of each sale you keep."),
    ("A candle costs ₹40 to make and sells for ₹100. What is the profit per candle?", ["₹40", "₹60", "₹140"], 1, "100 minus 40 is 60."),
    ("Fixed costs are...", ["Costs that stay the same, like shop rent", "Costs that change with each item", "Free"], 0, "Rent does not change with sales."),
    ("Variable costs are...", ["Costs that change with how many you make", "Costs that never change", "Salaries only"], 0, "Materials rise with output."),
    ("Fixed cost is ₹1,000 and profit is ₹50 per item. How many items to break even?", ["10", "20", "50"], 1, "1,000 divided by 50 is 20."),
    ("Which helps a young business grow?", ["Happy customers and good quality", "Hiding prices", "Copying exactly"], 0, "Reputation brings repeat sales."),
    ("Why test a product with a small batch first?", ["To learn before spending a lot", "To waste money", "To avoid customers"], 0, "Small tests reduce risk."),
    ("Reinvesting profit means...", ["Using some profit to grow the business", "Spending it all on treats", "Hiding it"], 0, "Growth needs fuel."),
    ("Competition means...", ["Others sell similar things", "No one sells anything", "Everything is free"], 0, "Think about how you are different."),
    ("Pricing too low can...", ["Hurt profit", "Always bring huge profit", "Stop all costs"], 0, "You must cover your costs."),
    ("A business plan lists...", ["Goals, costs, customers and how you will earn", "Only a name", "Only a logo"], 0, "It guides decisions."),
    ("You make a loss in the first month. What is a smart response?", ["Learn, adjust and try again", "Quit forever", "Blame customers"], 0, "Entrepreneurs learn from mistakes."),
]
P8 = [
    ("Phishing is...", ["Tricking people into sharing secrets through fake messages", "A kind of fishing sport", "A bank loan"], 0, "Scammers imitate real firms."),
    ("A caller says you are under 'digital arrest'. What should you do?", ["Hang up and tell a trusted adult", "Pay money", "Share your Aadhaar"], 0, "Real police do not demand money on video calls."),
    ("India's national cybercrime helpline number is...", ["1930", "100000", "555"], 0, "Report online fraud fast."),
    ("A message says 'Update your KYC now or your account closes', with a link. You should...", ["Contact your bank using its official app or number", "Click the link", "Share the OTP"], 0, "Use official channels only."),
    ("Which is a strong sign of a scam?", ["Pressure to act immediately", "A polite hello", "A shop receipt"], 0, "Scammers hurry you."),
    ("Two-factor authentication...", ["Adds a second step to prove it is you", "Doubles your money", "Hides your phone"], 0, "It protects accounts."),
    ("Public Wi-Fi is risky because...", ["Others may snoop on traffic", "It is too fast", "It costs money"], 0, "Avoid sensitive tasks on public Wi-Fi."),
    ("A friend's account suddenly asks you for money on chat. You should...", ["Call them to confirm first", "Send money quickly", "Share your PIN"], 0, "Accounts can be hacked."),
    ("Should you share your address and school on public social media?", ["No, keep personal details private", "Yes, always", "Only for prizes"], 0, "Oversharing helps scammers."),
    ("Which app source is safest?", ["The official app store", "A link from a stranger", "A forwarded file"], 0, "Fake apps can steal data."),
    ("A site offering a brand-new phone at 90% off is probably...", ["Too good to be true", "A great deal", "Government-approved"], 0, "Unbelievable offers are bait."),
    ("If you fell for a scam, the best step is to...", ["Tell an adult, contact your bank and report it", "Stay silent", "Pay again"], 0, "Quick reporting can stop losses."),
]

# ----------------------------------------------------------------- Games
SORT_S4 = [("🏪", "A shopkeeper sells biscuits", 0, "Selling goods is work."),
           ("👩‍🏫", "A teacher teaches the class", 0, "Teaching is work and earns a salary."),
           ("🎁", "Birthday money from an uncle", 1, "A gift is given freely."),
           ("🧑‍🌾", "A farmer sells vegetables", 0, "Growing and selling is work."),
           ("🌼", "Vishu Kaineettam from grandparents", 1, "Elders give it as a blessing."),
           ("🩺", "A doctor treats patients", 0, "Helping patients is work.")]
SORT_S5 = [("🍱", "Sharing your tiffin with a hungry friend", 0, "Sharing food is kind."),
           ("😝", "Laughing at a friend who has no money", 1, "Teasing hurts people."),
           ("🪙", "Putting a coin in a charity box", 0, "Charity helps others."),
           ("🙈", "Taking money from a friend's bag", 1, "Taking what is not yours is wrong."),
           ("✏️", "Lending a pencil to someone who forgot theirs", 0, "Small help is kind."),
           ("🚫", "Refusing to ever help anybody", 1, "Kind people help when they can.")]
SORT_S7 = [("🐷", "Keeping the piggy bank at home", 0, "Home is a safe place."),
           ("🧑‍🤝‍🧑", "Showing all your savings to strangers", 1, "Keep savings private."),
           ("🧮", "Counting change before leaving the shop", 0, "Counting avoids mistakes."),
           ("🔑", "Telling a friend your parent's phone PIN", 1, "PINs are secret."),
           ("🙋", "Telling a grown-up when you find money", 0, "A grown-up can help."),
           ("🚌", "Leaving coins on a bus seat", 1, "You could lose them.")]
SORT_E3 = [("💬", "A stranger in a game chat asks for your parent's card number", 1, "Never share card details with strangers."),
           ("📲", "Mom scans the shop's QR code to pay while you stand beside her", 0, "Paying with a trusted adult at a real shop is fine."),
           ("🎁", "A link says: You won a phone! Click now!", 1, "Free prizes that need a click are usually tricks."),
           ("🏦", "Keeping your savings in a bank account with a parent", 0, "A bank account held with a parent is a safe place."),
           ("📞", "A caller says: I am from the bank. Tell me your OTP.", 1, "Banks never ask for your OTP."),
           ("🗣️", "Telling a parent when someone online asks for money", 0, "Telling a trusted adult is always smart.")]
SORT_E5 = [("🔒", "Keeps your savings safe", 0, "Safe keeping is a bank's main job."),
           ("➕", "Pays you interest on savings", 0, "Interest rewards savers."),
           ("🏠", "Lends money for a fee called interest", 0, "Loans are how banks earn."),
           ("🍦", "Sells ice cream", 1, "That is a shop's job."),
           ("🚲", "Fixes bicycles", 1, "That is a mechanic's job."),
           ("📒", "Gives you a passbook or statement", 0, "It records money in and out.")]
SORT_P4 = [("🏢", "You own a tiny part of a company", 0, "That is a share."),
           ("🧺", "Many people pool money, and an expert fund manager invests it", 1, "That is a mutual fund."),
           ("🏦", "You lend money to a bank for a fixed time at a set rate", 2, "That is a fixed deposit."),
           ("🪙", "Coins or jewellery that people keep for the long term", 3, "That is gold."),
           ("📈", "Its price can swing a lot and it may pay dividends", 0, "Shares can swing and may pay dividends."),
           ("📅", "The return is known in advance if held to the end", 2, "Fixed deposits state the rate upfront.")]
SORT_P6 = [("💼", "Salary credited to your account", 0, "Earnings come in."),
           ("🧾", "Income tax paid", 1, "Tax goes out."),
           ("🏠", "Monthly rent", 1, "Rent goes out."),
           ("🎉", "A bonus from work", 0, "A bonus comes in."),
           ("🏦", "Interest earned on savings", 0, "Interest comes in."),
           ("💡", "Electricity bill", 1, "Bills go out.")]
SORT_P8 = [("📞", "A caller says you are under 'digital arrest' and must pay", 1, "Real police do not demand money on calls."),
           ("🏦", "You check your balance in the bank's official app", 0, "Official apps are safe."),
           ("🔗", "A link says: update KYC or your account closes today", 1, "Pressure plus a link means scam."),
           ("🔐", "Turning on two-factor login", 0, "It protects your accounts."),
           ("🎁", "A 90% off phone from an unknown site", 1, "Too good to be true."),
           ("👨‍👩‍👧", "Asking a parent before installing a new app", 0, "A second opinion is smart.")]

UPI_STEPS = ["Check the amount to pay", "Scan the shop's QR code with a parent", "Check the shop name shown",
             "Parent enters the PIN", "Wait for the success message"]

# ----------------------------------------------------------------- Lessons
LESSONS = [
    dict(id="s1", band="seed", title="Coins and Notes", art="🪙", blurb="Count out the right money for the shopkeeper.",
         badge=("Coin Counter", "🪙"),
         story=[("🪙", "Money is what we give to buy things we need and want."),
                ("🏪", "The shopkeeper gives us a toffee when we give the right money."),
                ("🔢", "Every coin and note has a number. A bigger number is more money.")],
         act=dict(type="coins", rounds=[dict(say="The toffee jar costs", target=17, item="🍬"),
                                        dict(say="The ice cream costs", target=26, item="🍦")]),
         talk="At the next shop visit, let your child pay and check the change.", bank=S1),
    dict(id="s2", band="seed", title="Needs and Wants", art="🍚", blurb="Sort things we must have from things that are nice to have.",
         badge=("Needs Ninja", "🥷"),
         story=[("💧", "A need is something we must have to stay healthy and safe, like food, water and medicine."),
                ("🎮", "A want is something nice to have, like toys and games."),
                ("🤔", "Smart kids ask: do I need it, or do I want it?")],
         act=dict(type="sort", labels=["Need", "Want"], items=[
             ("💧", "Clean water", 0, "We cannot live without water."), ("🎮", "Video game", 1, "Games are fun, but we can live without them."),
             ("🍚", "Rice and curry", 0, "Food gives us energy."), ("🍦", "Ice cream", 1, "Yummy, but it is a treat."),
             ("💊", "Medicine when sick", 0, "It helps us get better."), ("🚗", "Toy car", 1, "Toys are wants.")]),
         talk="Ask: of the things in our kitchen, which are needs and which are treats?", bank=S2),
    dict(id="s3", band="seed", title="My Piggy Bank", art="🐷", blurb="Save a little each day to reach a goal.",
         badge=("Piggy Pro", "🐷"),
         story=[("🐷", "A piggy bank keeps money safe until we need it."),
                ("⏳", "Saving takes patience. Small amounts add up."),
                ("🚲", "Pinku wants a ₹30 toy cycle. Let us help Pinku save.")],
         act=dict(type="piggy", goal=30, step=5, item="🚲", unit="Day", what="toy cycle"),
         talk="Start a real piggy bank. Agree a small goal and count the coins each week.", bank=S3),
    dict(id="s4", band="seed", title="Earning by Helping", art="💼", blurb="Learn where money comes from.",
         badge=("Earning Explorer", "💼"),
         story=[("🧑‍🌾", "People work to earn money."),
                ("🏪", "Shopkeepers, farmers, teachers and doctors all earn by helping others."),
                ("🎁", "Money can also come as a gift, like Vishu Kaineettam. A gift is not pay for work.")],
         act=dict(type="sort", labels=["Work", "Gift"], items=SORT_S4),
         talk="Ask your child to name three jobs in your neighbourhood and how each earns.", bank=S4),
    dict(id="s5", band="seed", title="Sharing and Giving", art="🤝", blurb="Small kindness helps a lot.",
         badge=("Kind Heart", "💛"),
         story=[("🤝", "Sharing means giving some of what we have to help others."),
                ("🍱", "Even small kindness counts, like sharing a snack or a pencil."),
                ("🍯", "The Share jar keeps a little money ready for helping.")],
         act=dict(type="sort", labels=["Kind", "Not kind"], items=SORT_S5),
         talk="Choose one small thing to give or share this week and do it together.", bank=S5),
    dict(id="s6", band="seed", title="Shopping and Change", art="🛍️", blurb="Pay the exact price and count your change.",
         badge=("Change Champion", "🛍️"),
         story=[("🏷️", "A price tag tells us how much something costs."),
                ("💵", "If we pay more than the price, the shopkeeper gives back change."),
                ("🧮", "Always count your change before you leave.")],
         act=dict(type="coins", rounds=[dict(say="The pencil box costs", target=12, item="✏️"),
                                        dict(say="The storybook costs", target=33, item="📚")]),
         talk="Give your child a small amount to buy something and count the change together.", bank=S6),
    dict(id="s7", band="seed", title="Money Safety", art="🔐", blurb="Keep money and secrets safe.",
         badge=("Safe Keeper", "🔐"),
         story=[("🔒", "Money is precious, so we keep it safe."),
                ("🧑‍🤝‍🧑", "Keep savings with a trusted grown-up. Never show them to strangers."),
                ("🔑", "PINs and passwords are secrets. We never tell them to friends or strangers.")],
         act=dict(type="sort", labels=["Safe", "Not safe"], items=SORT_S7),
         talk="Agree a family rule: who we tell when we find or lose money.", bank=S7),

    dict(id="e1", band="explore", title="Save, Spend, Share", art="🍯", blurb="Split your pocket money into three jars.",
         badge=("Jar Master", "🍯"),
         story=[("🍯", "Smart kids split pocket money into three jars: Save, Spend and Share."),
                ("💰", "Save is for big goals. Spend is for things now. Share is for helping others."),
                ("⚖️", "There is no single right split, but every jar should get something.")],
         act=dict(type="alloc", kind="jars", total=200, step=10,
                  cats=[("save", "Save"), ("spend", "Spend"), ("share", "Share")]),
         talk="Give pocket money in three small envelopes and let your child decide the split each month.", bank=E1),
    dict(id="e2", band="explore", title="The Nimbu Pani Stall", art="🍋", blurb="Set a price and find out if you make a profit.",
         badge=("Profit Pro", "📈"), badge_total=600,
         story=[("🍋", "Asha sells nimbu pani at a stall. Each glass costs her ₹6 to make."),
                ("🏷️", "Profit is the money left from sales after you pay your costs."),
                ("📈", "If the price is too low you lose money. If it is too high, fewer people buy.")],
         act=dict(type="stall", product="nimbu pani", unit="glass", cost=6, base=60, slope=2.0, start=12,
                  pmin=5, pmax=30, steps=(1, 5), target=600, good="Prices between ₹14 and ₹22 do well.",
                  days=[("Normal day", "🌤️", 1.0), ("Hot day", "☀️", 1.25), ("Rainy day", "🌧️", 0.6)]),
         talk="Plan a mini sale at home, such as lemonade or a book swap, and count costs and profit together.", bank=E2),
    dict(id="e3", band="explore", title="Safe Money, Scam Alert", art="🛡️", blurb="Spot the tricks and keep your money safe.",
         badge=("Scam Spotter", "🛡️"),
         story=[("📱", "Digital money is useful, but cheats try to trick people."),
                ("🔒", "Your UPI PIN and OTP are secrets. No bank or shop will ever ask for them."),
                ("🧑‍🤝‍🧑", "If something feels odd, stop and tell a trusted adult.")],
         act=dict(type="sort", labels=["Safe", "Scam alert"], items=SORT_E3),
         talk="Read a recent fraud message together and spot the tricks: hurry, prizes and requests for secrets.", bank=E3),
    dict(id="e4", band="explore", title="Budget Boss", art="📝", blurb="Plan a month of money and keep needs first.",
         badge=("Budget Boss", "📝"),
         story=[("📝", "A budget is a plan that tells your money where to go."),
                ("🏠", "Needs come first. Then savings. Then fun."),
                ("🧮", "Write down money in and money out so you can see where it goes.")],
         act=dict(type="alloc", kind="budget", total=400, step=20,
                  cats=[("school", "School things"), ("snacks", "Snacks"), ("fun", "Fun"), ("save", "Savings")]),
         talk="Let your child plan one month of pocket money on paper and review it at month end.", bank=E4),
    dict(id="e5", band="explore", title="Banks and Savings", art="🏦", blurb="See what a bank does and why interest matters.",
         badge=("Bank Buddy", "🏦"),
         story=[("🏦", "A bank keeps money safe and lends money to others."),
                ("➕", "When you keep money in a savings account, the bank pays you a little interest."),
                ("👨‍👩‍👧", "Children open accounts with a parent or guardian.")],
         act=dict(type="sort", labels=["Banks do this", "Banks do not"], items=SORT_E5),
         talk="Visit a branch or open the bank app together and read a statement line by line.", bank=E5),
    dict(id="e6", band="explore", title="UPI and Digital Payments", art="📲", blurb="Pay the safe way, step by step.",
         badge=("UPI Guard", "📲"),
         story=[("📱", "UPI lets us pay quickly with a phone."),
                ("🔢", "A PIN is needed only to send money. Nobody needs your PIN to give you money."),
                ("🔍", "Always check the name and amount before you pay.")],
         act=dict(type="order", steps=UPI_STEPS, title="Put the steps of a safe shop payment in order"),
         talk="Next time you pay by UPI, narrate each safe step out loud.", bank=E6),
    dict(id="e7", band="explore", title="Goals and Dreams", art="🎯", blurb="Break a big goal into weekly steps.",
         badge=("Goal Getter", "🎯"),
         story=[("🎯", "A goal says what you want, how much it costs, and by when."),
                ("🪜", "Big goals get easy when split into small weekly steps."),
                ("🎉", "Reaching a goal feels great and builds a habit.")],
         act=dict(type="piggy", goal=500, step=50, item="⚽", unit="Week", what="football"),
         talk="Write one goal with a price and a date on the fridge and track it weekly.", bank=E7),

    dict(id="p1", band="pioneer", title="Compound Magic", art="🌱", blurb="Watch small savings grow when interest earns interest.",
         badge=("Compound Wizard", "🧙"),
         story=[("🌱", "When your savings earn interest and that interest earns interest too, it is called compounding."),
                ("⏱️", "Time matters most. Starting early lets money grow for longer."),
                ("📊", "The rates in this game are examples, not promises. Real returns change.")],
         act=dict(type="grow"),
         talk="Open a recurring deposit or SIP calculator and compare 5 years with 15 years of the same monthly amount.", bank=P1),
    dict(id="p2", band="pioneer", title="The Practice Market", art="🏢", blurb="Spread practice money across made-up companies.",
         badge=("Risk Explorer", "🧭"),
         story=[("🏢", "A share is a small piece of ownership in a company."),
                ("🎢", "Share prices go up and down. Some companies swing much more than others."),
                ("🧺", "Spreading money across different things is called diversification. It makes the ride smoother. These companies are made up and the money is practice money.")],
         act=dict(type="market"),
         talk="Pick three brands your family uses and talk about what makes a business strong. Do not buy anything.", bank=P2),
    dict(id="p3", band="pioneer", title="Why ₹100 Buys Less", art="🍿", blurb="See how rising prices shrink money left idle.",
         badge=("Inflation Fighter", "🎈"),
         story=[("🍿", "Inflation means prices rise over time."),
                ("💸", "A snack that costs ₹100 today will cost more in the future."),
                ("🧭", "So money sitting in a cupboard buys less each year. Money needs a plan to keep up.")],
         act=dict(type="inflation"),
         talk="Ask grandparents what a cup of tea or a cinema ticket cost when they were young.", bank=P3),
    dict(id="p4", band="pioneer", title="Shares, Funds, FDs and Gold", art="🧺", blurb="Learn what each kind of investment is.",
         badge=("Smart Mixer", "🧺"),
         story=[("📚", "There are many ways to put money to work: shares, mutual funds, fixed deposits and gold."),
                ("⚖️", "Each has a different mix of risk and reward."),
                ("🧠", "This game teaches ideas only. It never tells anyone what to buy.")],
         act=dict(type="sort", labels=["Share", "Mutual fund", "Fixed deposit", "Gold"], items=SORT_P4),
         talk="Ask your child to explain, in their own words, the difference between a share and an FD.", bank=P4),
    dict(id="p5", band="pioneer", title="Credit, Loans and Debt", art="🏠", blurb="See what a loan really costs.",
         badge=("Debt Dodger", "🚧"),
         story=[("🏠", "A loan is borrowed money that must be paid back with interest."),
                ("📅", "Longer loans have smaller monthly payments but cost more interest in total."),
                ("⚠️", "Borrow for needs, with a plan, from trusted and regulated lenders.")],
         act=dict(type="loan"),
         talk="Look at a real EMI offer together and work out the total amount paid.", bank=P5),
    dict(id="p6", band="pioneer", title="Taxes and Salaries", art="🧾", blurb="Understand what happens to a salary.",
         badge=("Tax Whiz", "🧾"),
         story=[("🧾", "A payslip shows what you earn and what is taken out."),
                ("🏛️", "Taxes help pay for roads, schools, hospitals and more."),
                ("💡", "Knowing gross and net pay helps you plan.")],
         act=dict(type="sort", labels=["Comes in", "Goes out"], items=SORT_P6),
         talk="Show your child a bill with GST and point out the tax line.", bank=P6),
    dict(id="p7", band="pioneer", title="Start a Small Business", art="🕯️", blurb="Price handmade candles and learn about margins.",
         badge=("Young Founder", "🚀"), badge_total=9000,
         story=[("💡", "An entrepreneur starts a business to solve a problem."),
                ("🏭", "Income minus costs is profit. Some costs are fixed and some change with each item."),
                ("📈", "Price, quality and customers decide success.")],
         act=dict(type="stall", product="handmade candles", unit="candle", cost=40, base=120, slope=0.6, start=100,
                  pmin=40, pmax=200, steps=(5, 20), target=9000, good="Prices between ₹100 and ₹140 do well.",
                  days=[("Normal week", "🌤️", 1.0), ("Festival week", "🎆", 1.3), ("Quiet week", "🌧️", 0.7)]),
         talk="Brainstorm a tiny business your child could run for a day and list its costs.", bank=P7),
    dict(id="p8", band="pioneer", title="Online Fraud and Cyber Safety", art="🕵️", blurb="Spot modern scams and stay safe online.",
         badge=("Cyber Shield", "🕵️"),
         story=[("🕵️", "Scammers try to rush and scare people into sharing secrets."),
                ("🛡️", "Slow down. Check using official apps and numbers."),
                ("📣", "If something goes wrong, tell a trusted adult and report it quickly.")],
         act=dict(type="sort", labels=["Safe", "Scam alert"], items=SORT_P8),
         talk="Save the national cybercrime helpline number, 1930, in the family phone.", bank=P8),
]

LESSON_BY_ID = {l["id"]: l for l in LESSONS}
BAND_BY_ID = {b["id"]: b for b in BANDS}


def lessons_for(band):
    return [l for l in LESSONS if l["band"] == band]


def band_question_pool(band):
    pool = []
    for l in lessons_for(band):
        pool.extend(l["bank"])
    return pool


def total_questions():
    return sum(len(l["bank"]) for l in LESSONS)


# ----------------------------------------------------------------- Extra questions
# more_data holds extra questions (English and Malayalam side by side). Only the English part is used here.
try:
    from more_data import DATA as _MORE
except ImportError:
    _MORE = {}
for _l in LESSONS:
    _l["bank"] = list(_l["bank"]) + [(_t[0], _t[1], _t[2], _t[3]) for _t in _MORE.get(_l["id"], [])]

# ----------------------------------------------------------------- Self checks
assert len(LESSONS) == 22
for _l in LESSONS:
    assert len(_l["story"]) == 3, _l["id"]
    assert len(_l["bank"]) >= 12, (_l["id"], len(_l["bank"]))
    for _q in _l["bank"]:
        assert len(_q) == 4 and 0 <= _q[2] < len(_q[1]) and len(_q[1]) >= 3, (_l["id"], _q[0])
    if _l["act"]["type"] == "sort":
        for _i in _l["act"]["items"]:
            assert 0 <= _i[2] < len(_l["act"]["labels"]), (_l["id"], _i)
assert total_questions() >= 264
'''

_SOURCES['storage'] = r'''"""Tiny JSON store. One file, one entry per nickname.

Good for a family laptop or a classroom PC. For a public site with many
children, replace this module with a proper database and add parent consent
(see README, section Privacy).
"""
import contextlib
import datetime
import json
import os
import tempfile

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
PATH = os.path.join(DATA_DIR, "progress.json")

DEFAULT_PROFILE = {
    "band": "seed",
    "xp": 0,
    "streak": 0,
    "last_day": "",
    "done": {},          # lesson id -> best stars (1 to 3)
    "badges": [],
    "q_total": 0,
    "q_first": 0,
    "seconds": 0,
    "quick_best": {},    # band id -> best score out of 10
    "lessons_played": 0,
    "created": "",
}
DEFAULT_SETTINGS = {"theme": "auto", "listen": True, "lang": "en", "last_profile": ""}


def _read():
    try:
        with open(PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError):
        data = {}
    data.setdefault("profiles", {})
    data.setdefault("settings", dict(DEFAULT_SETTINGS))
    return data


def _write(data):
    os.makedirs(DATA_DIR, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=DATA_DIR, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, PATH)


def profile_names():
    return sorted(_read()["profiles"].keys())


def load_profile(name):
    p = dict(DEFAULT_PROFILE)
    p["done"] = {}
    p["badges"] = []
    p["quick_best"] = {}
    p.update(_read()["profiles"].get(name, {}))
    if not p["created"]:
        p["created"] = datetime.date.today().isoformat()
    return p


def save_profile(name, profile):
    with edit() as d:
        d["profiles"][name] = profile


def delete_profile(name):
    with edit() as d:
        d["profiles"].pop(name, None)


def settings():
    s = dict(DEFAULT_SETTINGS)
    s.update(_read()["settings"])
    return s


def save_settings(s):
    with edit() as d:
        d["settings"] = s


@contextlib.contextmanager
def edit():
    data = _read()
    yield data
    _write(data)


def export_json(name):
    return json.dumps({name: load_profile(name)}, ensure_ascii=False, indent=2)
'''

_SOURCES['ml_ui'] = r'''"""Malayalam interface strings. Key = the English sentence used in T(...), value = Malayalam with the same {placeholders}.
Please have a native Malayalam speaker proofread before launch."""

BANDS = {
    "seed": dict(name="വിത്തുകൾ", ages="5 മുതൽ 7 വയസ്സ് വരെ", note="ചിത്രങ്ങൾ, ശബ്ദങ്ങൾ, ചെറിയ ചുവടുകൾ", short="5 മുതൽ 7 വരെ"),
    "explore": dict(name="പര്യവേക്ഷകർ", ages="8 മുതൽ 10 വയസ്സ് വരെ", note="ശീലങ്ങൾ, ലാഭം, സുരക്ഷിതരായിരിക്കൽ", short="8 മുതൽ 10 വരെ"),
    "pioneer": dict(name="പ്രയാണികൾ", ages="11 മുതൽ 14 വയസ്സ് വരെ", note="വളർച്ച, റിസ്ക്, യഥാർത്ഥ ലോകം", short="11 മുതൽ 14 വരെ"),
}

UI = {
    # ---- theme and navigation
    "🌓 Auto": "🌓",
    "☀️ Light": "☀️",
    "🌙 Dark": "🌙",
    "🎒 Learn": "🎒 പഠനം",
    "⚡ Quiz": "⚡ ക്വിസ്",
    "🏆 Rewards": "🏆 സമ്മാനം",
    "👪 Parent": "👪 രക്ഷിതാവ്",
    "stars": "നക്ഷത്രം",
    "day streak": "ദിവസ പരമ്പര",
    "Lv {lv}": "{lv}",
    "level": "ലെവൽ",
    "lessons": "പാഠങ്ങൾ",
    "first-try right": "ആദ്യ ശ്രമത്തിൽ ശരി",
    "minutes": "മിനിറ്റ്",
    "none yet": "ഇതുവരെ ഇല്ല",
    "not yet": "ഇതുവരെ ഇല്ല",

    # ---- welcome and sign-in
    "Welcome to <b>EasyFin</b>. Learn how money works through stories, games and quizzes. Ages 5 to 14.":
        "<b>ഈസിഫിന്നിലേക്ക്</b> സ്വാഗതം. കഥകളിലൂടെയും ഗെയിമുകളിലൂടെയും ക്വിസുകളിലൂടെയും പണം എങ്ങനെ പ്രവർത്തിക്കുന്നു എന്ന് പഠിക്കാം. 5 മുതൽ 14 വയസ്സ് വരെ.",
    "Welcome back": "വീണ്ടും സ്വാഗതം",
    "or start a new learner": "അല്ലെങ്കിൽ പുതിയൊരു പഠിതാവിനെ ചേർക്കാം",
    "Open": "തുറക്കുക",
    "Pick a nickname (not your full name)": "ഒരു വിളിപ്പേര് തിരഞ്ഞെടുക്കൂ (മുഴുവൻ പേര് വേണ്ട)",
    "e.g. Aarav": "ഉദാ: ആരവ്",
    "Choose your age group": "നിങ്ങളുടെ പ്രായവിഭാഗം തിരഞ്ഞെടുക്കൂ",
    "My parent or guardian is with me and agrees": "എന്റെ രക്ഷിതാവ് എന്റെ കൂടെയുണ്ട്, സമ്മതവും ഉണ്ട്",
    "Let us start ➜": "നമുക്ക് തുടങ്ങാം ➜",
    "Please type a nickname.": "ഒരു വിളിപ്പേര് ടൈപ്പ് ചെയ്യൂ.",
    "A parent or guardian needs to be with you. Tick the box when they are.": "ഒരു രക്ഷിതാവ് കൂടെ ഉണ്ടായിരിക്കണം. അവർ ഉള്ളപ്പോൾ ബോക്സിൽ ടിക്ക് ചെയ്യൂ.",
    "That is not right. Try again.": "അത് ശരിയല്ല. വീണ്ടും ശ്രമിക്കൂ.",
    "Hi, I am Chintu!": "ഹായ്, ഞാൻ ചിന്റു!",
    "Practice money only. EasyFin teaches ideas and habits. It gives no investment advice or tips, and no real money moves here. Examples use made-up numbers.":
        "പരിശീലന പണം മാത്രം. ഈസിഫിൻ ആശയങ്ങളും ശീലങ്ങളും പഠിപ്പിക്കുന്നു. നിക്ഷേപ ഉപദേശമോ ടിപ്പുകളോ നൽകുന്നില്ല, യഥാർത്ഥ പണം ഇവിടെ നീങ്ങുന്നുമില്ല. ഉദാഹരണങ്ങളിൽ സാങ്കൽപ്പിക സംഖ്യകളാണ്.",

    # ---- home
    "Hi {name}!": "ഹായ് {name}!",
    "{done} of {total} lessons done. Keep going!": "{total} പാഠങ്ങളിൽ {done} എണ്ണം കഴിഞ്ഞു. മുന്നോട്ട് പോകൂ!",
    "Level {lv}, {xp} XP to level {next}": "ലെവൽ {lv}, ലെവൽ {next} ആകാൻ {xp} എക്സ്പി",
    "Quick Quiz": "ക്വിക്ക് ക്വിസ്",
    "10 mixed questions from the whole age group. Earn XP and try for 10 out of 10!": "പ്രായവിഭാഗത്തിലെ എല്ലാ പാഠങ്ങളിൽ നിന്നുമുള്ള 10 ചോദ്യങ്ങൾ. എക്സ്പി നേടൂ, 10 ൽ 10 നേടാൻ ശ്രമിക്കൂ!",
    "Start 10 questions ➜": "10 ചോദ്യങ്ങൾ തുടങ്ങാം ➜",
    "Play ➜": "കളിക്കാം ➜",
    "Play again": "വീണ്ടും കളിക്കാം",
    "Another round": "മറ്റൊരു റൗണ്ട്",
    "Back to lessons": "പാഠങ്ങളിലേക്ക് മടങ്ങാം",
    "◀ Back": "◀ പിന്നോട്ട്",
    "Next ▶": "അടുത്തത് ▶",
    "Let us play! 🎮": "നമുക്ക് കളിക്കാം! 🎮",
    "Take the quiz ➜": "ക്വിസ് എടുക്കാം ➜",
    "Next question ➜": "അടുത്ത ചോദ്യം ➜",
    "See my results ➜": "എന്റെ ഫലം കാണാം ➜",
    "Finish \"{title}\"": "\"{title}\" പൂർത്തിയാക്കുക",
    "Question {i} of {n}": "ചോദ്യം {i} / {n}",
    "{pool} questions in this group. Best score: <b>{best}</b>": "ഈ വിഭാഗത്തിൽ {pool} ചോദ്യങ്ങൾ. മികച്ച സ്കോർ: <b>{best}</b>",
    "What is {q}?": "{q} എന്താണ്?",
    "Great job!": "ഗംഭീരം!",
    "You got it!": "ശരിയായി!",
    "Not quite. That is okay. Try another answer.": "ഏകദേശം. സാരമില്ല. മറ്റൊരു ഉത്തരം ശ്രമിക്കൂ.",
    "Lesson complete!": "പാഠം പൂർത്തിയായി!",
    "{ok} of {n} right on the first try. +{xp} XP": "{n} ൽ {ok} ആദ്യ ശ്രമത്തിൽ ശരി. +{xp} എക്സ്പി",
    "Talk about it at home": "വീട്ടിൽ ഇതേക്കുറിച്ച് സംസാരിക്കൂ",
    "Quick Quiz done!": "ക്വിക്ക് ക്വിസ് കഴിഞ്ഞു!",
    "New badge: <b>{name}</b>.": "പുതിയ ബാഡ്ജ്: <b>{name}</b>.",

    # ---- rewards
    "Level {lv}": "ലെവൽ {lv}",
    "{xp} XP in total. {left} XP to the next level.": "ആകെ {xp} എക്സ്പി. അടുത്ത ലെവലിന് {left} എക്സ്പി കൂടി.",
    "Lesson badges": "പാഠ ബാഡ്ജുകൾ",
    "Special badges": "പ്രത്യേക ബാഡ്ജുകൾ",
    "First Step": "ആദ്യ ചുവട്",
    "Finish your first lesson": "ആദ്യത്തെ പാഠം പൂർത്തിയാക്കുക",
    "High Five": "ഹൈ ഫൈവ്",
    "Finish 5 lessons": "5 പാഠങ്ങൾ പൂർത്തിയാക്കുക",
    "On Fire": "തീപിടിച്ചു",
    "Learn 3 days in a row": "തുടർച്ചയായി 3 ദിവസം പഠിക്കുക",
    "Perfect Round": "പൂർണ്ണ റൗണ്ട്",
    "Get every quiz question right first time": "ഓരോ ക്വിസ് ചോദ്യവും ആദ്യ ശ്രമത്തിൽ ശരിയാക്കുക",
    "Power Up": "പവർ അപ്",
    "Earn 500 XP": "500 എക്സ്പി നേടുക",
    "Quiz Whiz": "ക്വിസ് വിസ്",
    "Score 10 out of 10 in a Quick Quiz": "ക്വിക്ക് ക്വിസിൽ 10 ൽ 10 നേടുക",
    "Seedling Graduate": "വിത്ത് ബിരുദധാരി",
    "Finish every Seedlings lesson": "വിത്തുകൾ വിഭാഗത്തിലെ എല്ലാ പാഠങ്ങളും പൂർത്തിയാക്കുക",
    "Explorer Graduate": "പര്യവേക്ഷക ബിരുദധാരി",
    "Finish every Explorers lesson": "പര്യവേക്ഷകർ വിഭാഗത്തിലെ എല്ലാ പാഠങ്ങളും പൂർത്തിയാക്കുക",
    "Pioneer Graduate": "പ്രയാണി ബിരുദധാരി",
    "Finish every Pioneers lesson": "പ്രയാണികൾ വിഭാഗത്തിലെ എല്ലാ പാഠങ്ങളും പൂർത്തിയാക്കുക",
    "Money Master": "പണ മാസ്റ്റർ",
    "Finish all 22 lessons": "22 പാഠങ്ങളും പൂർത്തിയാക്കുക",

    # ---- parent corner
    "Parent corner": "രക്ഷിതാക്കളുടെ കോർണർ",
    "A quick grown-up check, then you can see progress and settings.": "മുതിർന്നവർക്കുള്ള ഒരു ചെറിയ പരിശോധന, അതിനുശേഷം പുരോഗതിയും ക്രമീകരണങ്ങളും കാണാം.",
    "{name}'s progress": "{name} ന്റെ പുരോഗതി",
    "Age group: {band} · learning since {date}": "പ്രായവിഭാഗം: {band} · പഠനം തുടങ്ങിയത് {date}",
    "{d} of {n} lessons": "{n} പാഠങ്ങളിൽ {d}",
    "Lesson and conversation starter": "പാഠവും സംസാരം തുടങ്ങാനുള്ള ആശയവും",
    "Talk at home": "വീട്ടിൽ സംസാരിക്കാം",
    "Question bank": "ചോദ്യ ശേഖരം",
    "{q} questions across {l} lessons. Each play draws {k} at random, so replays feel fresh.": "{l} പാഠങ്ങളിലായി {q} ചോദ്യങ്ങൾ. ഓരോ തവണയും {k} ചോദ്യങ്ങൾ ക്രമരഹിതമായി വരും, അതിനാൽ വീണ്ടും കളിക്കുമ്പോഴും പുതുമ തോന്നും.",
    "Download progress (JSON)": "പുരോഗതി ഡൗൺലോഡ് ചെയ്യാം (JSON)",
    "Settings": "ക്രമീകരണങ്ങൾ",
    "🔊 Read aloud: on": "🔊 വായിച്ചു കേൾപ്പിക്കൽ: ഓൺ",
    "🔊 Read aloud: off": "🔊 വായിച്ചു കേൾപ്പിക്കൽ: ഓഫ്",
    "Switch learner": "പഠിതാവിനെ മാറ്റാം",
    "🔒 Lock": "🔒 ലോക്ക്",
    "Delete this learner's data": "ഈ പഠിതാവിന്റെ വിവരങ്ങൾ ഇല്ലാതാക്കുക",
    "This deletes all progress for this learner. It cannot be undone.": "ഇത് ഈ പഠിതാവിന്റെ എല്ലാ പുരോഗതിയും ഇല്ലാതാക്കും. തിരിച്ചെടുക്കാൻ കഴിയില്ല.",
    "Yes, delete": "അതെ, ഇല്ലാതാക്കുക",
    "Keep it": "സൂക്ഷിക്കുക",
    "Voice": "ശബ്ദം",
    "Privacy and safety": "സ്വകാര്യതയും സുരക്ഷയും",
    "Only a nickname and progress are stored, on this device. No ads, no chat, no real money. If you run this online for children, get verifiable parental consent as required by the DPDP Act and Rules, and keep the content educational only.":
        "വിളിപ്പേരും പുരോഗതിയും മാത്രമാണ് ഈ ഉപകരണത്തിൽ സൂക്ഷിക്കുന്നത്. പരസ്യങ്ങളില്ല, ചാറ്റില്ല, യഥാർത്ഥ പണവുമില്ല. ഇത് കുട്ടികൾക്കായി ഓൺലൈനിൽ നടത്തുകയാണെങ്കിൽ ഡിപിഡിപി നിയമവും ചട്ടങ്ങളും ആവശ്യപ്പെടുന്ന രക്ഷിതാവിന്റെ പരിശോധിക്കാവുന്ന സമ്മതം വാങ്ങുക, ഉള്ളടക്കം വിദ്യാഭ്യാസ ആവശ്യത്തിന് മാത്രമാക്കുക.",

    # ---- voice
    "Listen": "കേൾക്കാം",
    "This browser cannot read aloud.": "ഈ ബ്രൗസറിന് വായിച്ചു കേൾപ്പിക്കാൻ കഴിയില്ല.",
    "No Malayalam voice on this device. A parent can add a natural voice in Parent corner.": "ഈ ഉപകരണത്തിൽ മലയാളം ശബ്ദം ഇല്ല. രക്ഷിതാവിന് രക്ഷിതാക്കളുടെ കോർണറിൽ സ്വാഭാവിക ശബ്ദം ചേർക്കാം.",
    "Malayalam voice: using the browser voice. Add a Sarvam key in the app secrets for a natural voice.": "മലയാളം ശബ്ദം: ബ്രൗസറിന്റെ ശബ്ദമാണ് ഉപയോഗിക്കുന്നത്. സ്വാഭാവിക ശബ്ദത്തിന് ആപ്പ് സീക്രട്ടുകളിൽ സർവം കീ ചേർക്കുക.",
    "Malayalam voice: saved audio clips are installed.": "മലയാളം ശബ്ദം: സൂക്ഷിച്ച ഓഡിയോ ക്ലിപ്പുകൾ ഉപയോഗിക്കുന്നു.",
    "Malayalam voice: Sarvam is connected.": "മലയാളം ശബ്ദം: സർവം ബന്ധിപ്പിച്ചിരിക്കുന്നു.",
    "Last problem: {err}": "അവസാനത്തെ പ്രശ്നം: {err}",

    # ---- game common
    "Not quite. Think again.": "ഏകദേശം. ഒന്നുകൂടി ആലോചിക്കൂ.",
    "Yes!": "ശരി!",
    "All sorted! You made {n} slip.": "എല്ലാം തരംതിരിച്ചു! {n} തെറ്റ് പറ്റി.",
    "All sorted! You made {n} slips.": "എല്ലാം തരംതിരിച്ചു! {n} തെറ്റുകൾ പറ്റി.",
    "Item {n} of {total}. Where does it belong?": "{total} ൽ {n}-ാമത്തെ സാധനം. ഇത് എവിടെ ചേരും?",
    "{what}: {have} of {need}": "{what}: {need} ൽ {have}",
    "Try different years. Years tried": "വ്യത്യസ്ത വർഷങ്ങൾ പരീക്ഷിക്കൂ. പരീക്ഷിച്ച വർഷങ്ങൾ",
    "Years played": "കളിച്ച വർഷങ്ങൾ",
    "Try other settings. Combinations tried": "മറ്റ് ക്രമീകരണങ്ങൾ പരീക്ഷിക്കൂ. പരീക്ഷിച്ച കോമ്പിനേഷനുകൾ",

    # ---- coins
    "Tap coins and notes": "നാണയങ്ങളിലും നോട്ടുകളിലും തൊടൂ",
    "you have paid": "നിങ്ങൾ കൊടുത്തത്",
    "↩ Undo": "↩ തിരികെ",
    "Clear": "മായ്ക്കുക",
    "Check ✓": "പരിശോധിക്കൂ ✓",
    "Perfect! You paid exactly the right amount.": "ഗംഭീരം! നിങ്ങൾ കൃത്യമായ തുക തന്നെ കൊടുത്തു.",
    "Yes! Exactly right. Here comes the next one.": "ശരി! കൃത്യം. ഇതാ അടുത്തത്.",
    "Not enough yet. You need {amt} more.": "ഇത് മതിയാകില്ല. {amt} കൂടി വേണം.",
    "That is {amt} too much. Press Undo and try again.": "{amt} കൂടുതലായി. തിരികെ അമർത്തി വീണ്ടും ശ്രമിക്കൂ.",

    # ---- piggy
    "Goal: a {what} for {amt}": "ലക്ഷ്യം: {amt} വിലയുള്ള {what}",
    "Save {amt} this {unit} 🪙": "ഈ {unit} {amt} സമ്പാദിക്കാം 🪙",
    "Small, regular steps reach the goal.": "ചെറിയ പതിവ് ചുവടുകൾ ലക്ഷ്യത്തിലെത്തിക്കും.",
    "You reached {goal} in {n} {units} by saving {step} each time. Patience paid off!": "ഓരോ തവണയും {step} വീതം സമ്പാദിച്ച് നിങ്ങൾ {n} {units} കൊണ്ട് {goal} നേടി. ക്ഷമയ്ക്ക് ഫലം കിട്ടി!",

    # ---- alloc
    "left to place out of {total}": "{total} ൽ വിഭജിക്കാൻ ബാക്കി",
    "Check my plan ✓": "എന്റെ പദ്ധതി പരിശോധിക്കൂ ✓",
    "<b>{pct}%</b> of it": "അതിന്റെ <b>{pct}%</b>",
    "You still have {amt} to place. Every rupee needs a job.": "നിങ്ങൾക്ക് ഇനിയും {amt} വിഭജിക്കാനുണ്ട്. ഓരോ രൂപയ്ക്കും ഒരു ജോലി വേണം.",
    "Give every jar at least a little. Even Share and Save matter.": "ഓരോ ഭരണിക്കും കുറച്ചെങ്കിലും കൊടുക്കൂ. പങ്കിടലും സമ്പാദ്യവും പ്രധാനമാണ്.",
    "Try to save at least a fifth of your money. Future you will say thanks!": "പണത്തിന്റെ അഞ്ചിലൊന്നെങ്കിലും സമ്പാദിക്കാൻ ശ്രമിക്കൂ. ഭാവിയിലെ നിങ്ങൾ നന്ദി പറയും!",
    "Nice split. Every jar has a job and your savings are growing.": "നല്ല വിഭജനം. ഓരോ ഭരണിക്കും ഒരു ജോലിയുണ്ട്, നിങ്ങളുടെ സമ്പാദ്യം വളരുന്നു.",
    "Needs come first. Give School things at least a quarter of your money.": "ആവശ്യങ്ങൾ ആദ്യം. സ്കൂൾ സാധനങ്ങൾക്ക് പണത്തിന്റെ കാൽഭാഗമെങ്കിലും കൊടുക്കൂ.",
    "Add at least a tenth to Savings, so you can handle surprises.": "അപ്രതീക്ഷിത കാര്യങ്ങൾ നേരിടാൻ സമ്പാദ്യത്തിന് പത്തിലൊന്നെങ്കിലും ചേർക്കൂ.",
    "Snacks and Fun together are more than half. Can you trim a little?": "പലഹാരങ്ങളും വിനോദവും ചേർന്നാൽ പകുതിയിലധികമായി. കുറച്ചു കുറയ്ക്കാമോ?",
    "A balanced budget! Needs first, then savings, then fun.": "സന്തുലിതമായ ബജറ്റ്! ആദ്യം ആവശ്യങ്ങൾ, പിന്നെ സമ്പാദ്യം, അതിനുശേഷം വിനോദം.",

    # ---- stall
    "{name} at the {product} stall. Each {unit} costs {cost} to make.": "{name} {product} കടയിൽ. ഓരോ {unit} ഉണ്ടാക്കാനും {cost} ചെലവാകും.",
    "price per {unit}": "ഒരു {unit} ന്റെ വില",
    "Open the stall ({emoji})": "കട തുറക്കൂ ({emoji})",
    "Try another day ➜": "മറ്റൊരു ദിവസം പരീക്ഷിക്കൂ ➜",
    "Goal today: a profit of at least <b>{goal}</b> (try {n} of 4)": "ഇന്നത്തെ ലക്ഷ്യം: കുറഞ്ഞത് <b>{goal}</b> ലാഭം (ശ്രമം {n} / 4)",
    "Sold": "വിറ്റത്",
    "Money in": "വരവ്",
    "Costs": "ചെലവ്",
    "Profit": "ലാഭം",
    "Goal reached! Profit is what is left after costs, and you found a price customers like.": "ലക്ഷ്യം നേടി! ചെലവ് കഴിഞ്ഞ് ബാക്കിയാകുന്നതാണ് ലാഭം, ഉപഭോക്താക്കൾക്ക് ഇഷ്ടപ്പെടുന്ന ഒരു വില നിങ്ങൾ കണ്ടെത്തി.",
    "A loss. You paid more to make the goods than you earned. Raise the price a little.": "നഷ്ടം. സാധനങ്ങൾ ഉണ്ടാക്കാൻ നിങ്ങൾ നേടിയതിനേക്കാൾ കൂടുതൽ ചെലവാക്കി. വില കുറച്ചുകൂടി ഉയർത്തൂ.",
    "Nobody bought anything. That price is too high. Try lowering it.": "ആരും ഒന്നും വാങ്ങിയില്ല. ആ വില വളരെ കൂടുതലാണ്. കുറച്ചു നോക്കൂ.",
    "Close. On a day like this, prices between {lo} and {hi} reach the goal.": "അടുത്തെത്തി. ഇതുപോലൊരു ദിവസം {lo} നും {hi} നും ഇടയിലുള്ള വില ലക്ഷ്യത്തിലെത്തിക്കും.",
    "This is a tough day. Do your best price, then try another day.": "ഇത് ബുദ്ധിമുട്ടുള്ള ദിവസമാണ്. കഴിയുന്നത്ര നല്ല വില വെക്കൂ, എന്നിട്ട് മറ്റൊരു ദിവസം പരീക്ഷിക്കൂ.",
    "That is 4 tries. Real shopkeepers keep adjusting too. Let us move on to the quiz.": "4 ശ്രമം കഴിഞ്ഞു. യഥാർത്ഥ കടക്കാരും വില ക്രമീകരിച്ചുകൊണ്ടിരിക്കും. നമുക്ക് ക്വിസിലേക്ക് പോകാം.",

    # ---- order
    "Tap the steps below in order": "താഴെയുള്ള ഘട്ടങ്ങൾ ക്രമത്തിൽ തൊടൂ",
    "All in the right order. Safe paying habit unlocked!": "എല്ലാം ശരിയായ ക്രമത്തിൽ. സുരക്ഷിതമായി പണം അടയ്ക്കുന്ന ശീലം നേടി!",
    "Not that one yet. What happens first, before money moves?": "ഇത് ഇപ്പോഴല്ല. പണം നീങ്ങും മുമ്പ് ആദ്യം എന്താണ് സംഭവിക്കുന്നത്?",

    # ---- compound growth
    "Monthly saving": "പ്രതിമാസ സമ്പാദ്യം",
    "Example yearly growth (not a promise)": "ഉദാഹരണ വാർഷിക വളർച്ച (വാഗ്ദാനമല്ല)",
    "Years": "വർഷം",
    "after {years} years": "{years} വർഷം കഴിഞ്ഞ്",
    "You put in {amt}": "നിങ്ങൾ ഇട്ടത് {amt}",
    "Growth on growth: {amt}": "വളർച്ചയുടെ മേൽ വളർച്ച: {amt}",
    "Example only. Real returns go up and down and are never guaranteed.": "ഉദാഹരണം മാത്രം. യഥാർത്ഥ ആദായം കൂടിയും കുറഞ്ഞും ഇരിക്കും, ഒരിക്കലും ഉറപ്പില്ല.",
    "Start 5 years later and the same saving grows to only {amt}. Starting early is a superpower.": "5 വർഷം വൈകി തുടങ്ങിയാൽ അതേ സമ്പാദ്യം {amt} ആയി മാത്രമേ വളരൂ. നേരത്തെ തുടങ്ങുന്നത് ഒരു മഹാശക്തിയാണ്.",

    # ---- market
    "practice money left to place (made-up companies)": "വിഭജിക്കാൻ ബാക്കിയുള്ള പരിശീലന പണം (സാങ്കൽപ്പിക കമ്പനികൾ)",
    "Chintu Chai Co.": "ചിന്റു ചായ കമ്പനി",
    "Rocket Phones": "റോക്കറ്റ് ഫോൺസ്",
    "Green Rickshaw": "ഗ്രീൻ റിക്ഷ",
    "Kerala Bananas": "കേരള ബനാനാസ്",
    "Steady seller": "സ്ഥിരമായി വിറ്റുപോകുന്നത്",
    "Wild swings": "വലിയ ചാഞ്ചാട്ടം",
    "Medium swings": "ഇടത്തരം ചാഞ്ചാട്ടം",
    "Boom year": "തിളങ്ങുന്ന വർഷം",
    "Crash year": "തകർച്ചയുടെ വർഷം",
    "Normal year": "സാധാരണ വർഷം",
    "Made-up companies and made-up years. This is a learning game, never advice to buy anything.": "കമ്പനികളും വർഷങ്ങളും സാങ്കൽപ്പികമാണ്. ഇത് പഠിക്കാനുള്ള ഗെയിമാണ്, ഒന്നും വാങ്ങാനുള്ള ഉപദേശമല്ല.",
    "Company": "കമ്പനി",
    "Year result": "വർഷത്തെ ഫലം",
    "Your practice money is now {value} ({change}).": "നിങ്ങളുടെ പരിശീലന പണം ഇപ്പോൾ {value} ആണ് ({change}).",
    "You spread your money across several companies, so no single bad year hurt too much. That is diversification.": "നിങ്ങൾ പണം പല കമ്പനികളിൽ ഭാഗിച്ചു, അതിനാൽ ഒരു മോശം വർഷവും അധികം വേദനിപ്പിച്ചില്ല. അതാണ് വൈവിധ്യവൽക്കരണം.",
    "Your money sat in few companies, so results swung more. Spreading across more companies usually smooths the ride.": "നിങ്ങളുടെ പണം കുറച്ച് കമ്പനികളിൽ ആയിരുന്നു, അതുകൊണ്ട് ഫലം കൂടുതൽ ചാഞ്ചാടി. കൂടുതൽ കമ്പനികളിൽ ഭാഗിച്ചാൽ യാത്ര സുഗമമാകും.",

    "Place all your practice money to start the years.": "വർഷങ്ങൾ തുടങ്ങാൻ നിങ്ങളുടെ പരിശീലന പണം മുഴുവൻ വിഭജിക്കൂ.",
    "Stars": "നക്ഷത്രങ്ങൾ",

    # ---- inflation
    "Years from now": "ഇപ്പോൾ മുതൽ വർഷങ്ങൾ",
    "Example yearly price rise": "ഉദാഹരണ വാർഷിക വിലക്കയറ്റം",
    "what a ₹100 snack costs in {years} years": "{years} വർഷം കഴിയുമ്പോൾ ₹100 ന്റെ പലഹാരത്തിന്റെ വില",
    "₹100 kept idle will then buy only this much of today's snack:": "വെറുതെ വെച്ച ₹100 കൊണ്ട് അപ്പോൾ ഇന്നത്തെ പലഹാരത്തിന്റെ ഇത്രയും ഭാഗം മാത്രമേ വാങ്ങാൻ കഴിയൂ:",
    "Example rates for learning. Real inflation changes from year to year.": "പഠിക്കാനുള്ള ഉദാഹരണ നിരക്കുകൾ. യഥാർത്ഥ വിലക്കയറ്റം ഓരോ വർഷവും മാറും.",

    # ---- loan
    "Amount borrowed": "കടം വാങ്ങിയ തുക",
    "Example yearly interest rate": "ഉദാഹരണ വാർഷിക പലിശ നിരക്ക്",
    "Years to repay": "തിരിച്ചടയ്ക്കാനുള്ള വർഷം",
    "EMI, paid every month": "ഇഎംഐ, ഓരോ മാസവും അടയ്ക്കുന്നത്",
    "You borrow": "നിങ്ങൾ കടം വാങ്ങുന്നത്",
    "You pay back": "നിങ്ങൾ തിരിച്ചടയ്ക്കുന്നത്",
    "Extra cost (interest)": "അധിക ചെലവ് (പലിശ)",
    "{pct}% of what you pay is interest": "നിങ്ങൾ അടയ്ക്കുന്നതിന്റെ {pct}% പലിശയാണ്",
    "Example only. Borrow from trusted, regulated lenders and ask a grown-up first.": "ഉദാഹരണം മാത്രം. വിശ്വസനീയവും നിയന്ത്രണത്തിലുള്ളതുമായ വായ്പാദാതാക്കളിൽ നിന്ന് മാത്രം കടം വാങ്ങുക, ആദ്യം ഒരു മുതിർന്ന ആളോട് ചോദിക്കുക.",
}
'''

_SOURCES['ml_lessons'] = r'''"""Malayalam lesson text: titles, stories, talk prompts, badge names and game labels.

Everything lines up by position with content.py (same order of items, steps, days and categories).
Please have a native Malayalam speaker proofread before launch.
"""

META = {
    # ------------------------------------------------------------- Seedlings
    "s1": dict(
        title="നാണയങ്ങളും നോട്ടുകളും",
        blurb="കടക്കാരന് ശരിയായ പണം എണ്ണി കൊടുക്കാം.",
        badge="നാണയ വിദഗ്ധൻ",
        story=["നമുക്ക് വേണ്ടതും ഇഷ്ടമുള്ളതുമായ സാധനങ്ങൾ വാങ്ങാൻ നമ്മൾ കൊടുക്കുന്നതാ പൈസ.",
               "ശരിയായ പൈസ കൊടുത്താൽ കടക്കാരൻ നമുക്ക് മിഠായി തരും.",
               "ഓരോ നാണയത്തിനും നോട്ടിനും ഒരു സംഖ്യ ഉണ്ട്. വലിയ സംഖ്യ ആണെങ്കിൽ കൂടുതൽ പൈസ."],
        talk="അടുത്ത തവണ കടയിൽ പോകുമ്പോൾ കുട്ടി തന്നെ പണം കൊടുക്കട്ടെ, ബാക്കി തുക പരിശോധിക്കട്ടെ.",
        act=dict(say=["മിഠായി ഭരണിയുടെ വില", "ഐസ്ക്രീമിന്റെ വില"]),
    ),
    "s2": dict(
        title="ആവശ്യങ്ങളും ആഗ്രഹങ്ങളും",
        blurb="ജീവിക്കാൻ വേണ്ടതും ഉണ്ടെങ്കിൽ നല്ലതെന്ന് തോന്നുന്നതും വേർതിരിക്കാം.",
        badge="ആവശ്യ നിൻജ",
        story=["ആരോഗ്യത്തോടെ സേഫായി ഇരിക്കാൻ നമുക്ക് തീർച്ചയായും വേണ്ടതാ ആവശ്യം, ഉദാഹരണത്തിന് ഭക്ഷണം, വെള്ളം, മരുന്ന്.",
               "ഉണ്ടെങ്കിൽ സന്തോഷം തോന്നുന്നതാ ആഗ്രഹം, ഉദാഹരണത്തിന് കളിപ്പാട്ടവും ഗെയിമും.",
               "മിടുക്കരായ കുട്ടികൾ ചോദിക്കും: ഇത് എനിക്ക് ശരിക്കും വേണ്ടതാണോ, അതോ വെറുതെ വേണം എന്ന് തോന്നുന്നതാണോ?"],
        talk="അടുക്കളയിലെ സാധനങ്ങളിൽ ഏതൊക്കെ ആവശ്യങ്ങളാണ്, ഏതൊക്കെ ട്രീറ്റുകളാണ് എന്ന് കുട്ടിയോട് ചോദിക്കുക.",
        act=dict(labels=["ആവശ്യം", "ആഗ്രഹം"], items=[
            ("ശുദ്ധജലം", "വെള്ളം ഇല്ലാതെ നമുക്ക് ജീവിക്കാൻ പറ്റില്ല."),
            ("വീഡിയോ ഗെയിം", "ഗെയിം രസമാ, പക്ഷേ അതില്ലാതെയും ജീവിക്കാം."),
            ("ചോറും കറിയും", "ഭക്ഷണം കഴിച്ചാലേ നമുക്ക് ഉഷാറുണ്ടാകൂ."),
            ("ഐസ്ക്രീം", "രുചിയുണ്ട്, പക്ഷേ അതൊരു ട്രീറ്റാ."),
            ("അസുഖം വരുമ്പോഴുള്ള മരുന്ന്", "അസുഖം മാറാൻ അത് വേണം."),
            ("കളിപ്പാട്ട കാർ", "കളിപ്പാട്ടം ഒരു ആഗ്രഹമാ.")]),
    ),
    "s3": dict(
        title="എന്റെ കുടുക്ക",
        blurb="ലക്ഷ്യത്തിലെത്താൻ ദിവസവും കുറച്ചു വീതം സമ്പാദിക്കാം.",
        badge="കുടുക്ക വിദഗ്ധൻ",
        story=["പൈസ വേണ്ടി വരുന്നത് വരെ സേഫായി സൂക്ഷിക്കാനുള്ളതാ കുടുക്ക.",
               "സമ്പാദിക്കാൻ ക്ഷമ വേണം. ചെറിയ തുകകൾ കൂടിക്കൂടി വലുതാകും.",
               "പിങ്കുവിന് ₹30 വിലയുള്ള ഒരു കളിപ്പാട്ട സൈക്കിൾ വേണം. പിങ്കുവിനെ നമുക്ക് സഹായിക്കാം."],
        talk="ഒരു യഥാർത്ഥ കുടുക്ക തുടങ്ങുക. ചെറിയൊരു ലക്ഷ്യം തീരുമാനിച്ച് ആഴ്ചതോറും നാണയങ്ങൾ എണ്ണുക.",
        act=dict(unit="ദിവസം", unit_pl="ദിവസം", what="കളിപ്പാട്ട സൈക്കിൾ"),
    ),
    "s4": dict(
        title="സഹായിച്ച് സമ്പാദിക്കാം",
        blurb="പണം എവിടെ നിന്ന് വരുന്നു എന്ന് അറിയാം.",
        badge="സമ്പാദ്യ അന്വേഷകൻ",
        story=["ആളുകൾ പൈസ ഉണ്ടാക്കാൻ ജോലി ചെയ്യുന്നു.",
               "കടക്കാരും കർഷകരും ടീച്ചർമാരും ഡോക്ടർമാരും എല്ലാവരും മറ്റുള്ളവരെ സഹായിച്ചാ പൈസ ഉണ്ടാക്കുന്നത്.",
               "വിഷുക്കൈനീട്ടം പോലെ പൈസ സമ്മാനമായും കിട്ടാം. സമ്മാനം ജോലിക്കുള്ള കൂലിയല്ല."],
        talk="നിങ്ങളുടെ പരിസരത്തെ മൂന്ന് ജോലികൾ പറയാനും ഓരോന്നിനും എങ്ങനെ പണം കിട്ടുന്നു എന്ന് വിശദീകരിക്കാനും കുട്ടിയോട് പറയുക.",
        act=dict(labels=["ജോലി", "സമ്മാനം"], items=[
            ("ബിസ്കറ്റ് വിൽക്കുന്ന കടക്കാരൻ", "സാധനം വിൽക്കുന്നത് ഒരു ജോലിയാ."),
            ("ക്ലാസ്സിൽ പഠിപ്പിക്കുന്ന അധ്യാപിക", "പഠിപ്പിക്കുന്നത് ജോലിയാ, അതിന് ശമ്പളം കിട്ടും."),
            ("അമ്മാവൻ തരുന്ന പിറന്നാൾ പണം", "സമ്മാനം സ്നേഹം കൊണ്ട് തരുന്നതാ."),
            ("പച്ചക്കറി വിൽക്കുന്ന കർഷകൻ", "കൃഷി ചെയ്ത് വിൽക്കുന്നത് ജോലിയാ."),
            ("മുത്തശ്ശീമുത്തശ്ശന്മാർ തരുന്ന വിഷുക്കൈനീട്ടം", "വലിയവർ അനുഗ്രഹമായി തരുന്നതാ അത്."),
            ("രോഗികളെ ചികിത്സിക്കുന്ന ഡോക്ടർ", "രോഗികളെ സഹായിക്കുന്നത് ജോലിയാ.")]),
    ),
    "s5": dict(
        title="പങ്കുവെക്കലും കൊടുക്കലും",
        blurb="ചെറിയ ദയയും വലിയ സഹായമാണ്.",
        badge="നല്ല മനസ്സ്",
        story=["നമ്മുടെ കൈയിൽ ഉള്ളതിൽ കുറച്ച് മറ്റുള്ളവരെ സഹായിക്കാൻ കൊടുക്കുന്നതാ പങ്കുവെക്കൽ.",
               "ഒരു പലഹാരമോ പെൻസിലോ പങ്കുവെക്കുന്നത് പോലുള്ള ചെറിയ നന്മയ്ക്കും വിലയുണ്ട്.",
               "സഹായിക്കാൻ വേണ്ടി കുറച്ച് പൈസ മാറ്റിവെക്കാനുള്ളതാ പങ്കുവെക്കൽ ഭരണി."],
        talk="ഈ ആഴ്ച ഒരു ചെറിയ കാര്യം മറ്റൊരാൾക്ക് കൊടുക്കാനോ പങ്കുവെക്കാനോ തിരഞ്ഞെടുത്ത് ഒരുമിച്ച് ചെയ്യുക.",
        act=dict(labels=["നല്ല പ്രവൃത്തി", "നല്ലതല്ലാത്ത പ്രവൃത്തി"], items=[
            ("വിശക്കുന്ന കൂട്ടുകാരനുമായി ചോറ്റുപാത്രം പങ്കുവെക്കുന്നു", "ഭക്ഷണം പങ്കുവെക്കുന്നത് നല്ല കാര്യമാ."),
            ("പണമില്ലാത്ത കൂട്ടുകാരനെ കളിയാക്കുന്നു", "കളിയാക്കിയാൽ മറ്റുള്ളവർക്ക് വിഷമമാകും."),
            ("ദാനപ്പെട്ടിയിൽ ഒരു നാണയം ഇടുന്നു", "ദാനം മറ്റുള്ളവർക്ക് സഹായമാകും."),
            ("കൂട്ടുകാരന്റെ ബാഗിൽ നിന്ന് പണം എടുക്കുന്നു", "നമ്മുടേതല്ലാത്തത് എടുക്കുന്നത് തെറ്റാ."),
            ("പെൻസിൽ മറന്ന ഒരാൾക്ക് സ്വന്തം പെൻസിൽ കടം കൊടുക്കുന്നു", "ചെറിയ സഹായവും നല്ല കാര്യമാ."),
            ("ആരെയും ഒരിക്കലും സഹായിക്കില്ലെന്ന് പറയുന്നു", "നല്ല മനസ്സുള്ളവർ പറ്റുന്നിടത്തോളം സഹായിക്കും.")]),
    ),
    "s6": dict(
        title="ഷോപ്പിങ്ങും ബാക്കി തുകയും",
        blurb="കൃത്യമായ വില കൊടുക്കാം, ബാക്കി തുക എണ്ണി നോക്കാം.",
        badge="ബാക്കി തുക ചാമ്പ്യൻ",
        story=["ഒരു സാധനത്തിന് എത്ര രൂപയാണെന്ന് വിലച്ചീട്ട് പറയും.",
               "വിലയെക്കാൾ കൂടുതൽ കൊടുത്താൽ കടക്കാരൻ ബാക്കി പൈസ തിരിച്ചു തരും.",
               "പോകുന്നതിന് മുൻപ് ബാക്കി പൈസ എപ്പോഴും എണ്ണി നോക്കണം."],
        talk="ചെറിയൊരു തുക കൊടുത്ത് എന്തെങ്കിലും വാങ്ങാൻ പറയുക, ബാക്കി തുക ഒരുമിച്ച് എണ്ണുക.",
        act=dict(say=["പെൻസിൽ ബോക്സിന്റെ വില", "കഥാപുസ്തകത്തിന്റെ വില"]),
    ),
    "s7": dict(
        title="പണത്തിന്റെ സുരക്ഷ",
        blurb="പണവും രഹസ്യങ്ങളും സുരക്ഷിതമായി സൂക്ഷിക്കാം.",
        badge="സുരക്ഷാ കാവൽക്കാരൻ",
        story=["പൈസ വിലപ്പെട്ടതാ, അതുകൊണ്ട് നമ്മൾ അത് സേഫായി സൂക്ഷിക്കും.",
               "സമ്പാദ്യം വിശ്വാസമുള്ള ഒരു വലിയ ആളുടെ അടുത്ത് സൂക്ഷിക്കണം. അപരിചിതരെ ഒരിക്കലും കാണിക്കരുത്.",
               "പിന്നും പാസ്‌വേഡും രഹസ്യമാ. കൂട്ടുകാരോടോ അപരിചിതരോടോ ഒരിക്കലും പറയരുത്."],
        talk="പണം കിട്ടുകയോ നഷ്ടപ്പെടുകയോ ചെയ്താൽ ആരോടാണ് പറയേണ്ടതെന്ന് വീട്ടിൽ ഒരു നിയമം തീരുമാനിക്കുക.",
        act=dict(labels=["സുരക്ഷിതം", "സുരക്ഷിതമല്ല"], items=[
            ("കുടുക്ക വീട്ടിൽ സൂക്ഷിക്കുന്നു", "വീട് സേഫായ സ്ഥലമാ."),
            ("സമ്പാദ്യം മുഴുവൻ അപരിചിതരെ കാണിക്കുന്നു", "സമ്പാദ്യം വേറെ ആരും അറിയരുത്."),
            ("കടയിൽ നിന്ന് ഇറങ്ങുംമുമ്പ് ബാക്കി തുക എണ്ണുന്നു", "എണ്ണി നോക്കിയാൽ തെറ്റ് വരില്ല."),
            ("മാതാപിതാക്കളുടെ ഫോൺ പിൻ കൂട്ടുകാരനോട് പറയുന്നു", "പിൻ ഒരു രഹസ്യമാ."),
            ("പണം കിട്ടിയാൽ മുതിർന്ന ഒരാളോട് പറയുന്നു", "വലിയ ആൾക്ക് സഹായിക്കാൻ പറ്റും."),
            ("ബസ് സീറ്റിൽ നാണയങ്ങൾ വെച്ചിട്ട് പോകുന്നു", "അത് കളഞ്ഞുപോയെന്ന് വരാം.")]),
    ),

    # ------------------------------------------------------------- Explorers
    "e1": dict(
        title="സമ്പാദിക്കാം, ചെലവാക്കാം, പങ്കുവെക്കാം",
        blurb="പോക്കറ്റ് മണി മൂന്ന് ഭരണികളായി വിഭജിക്കാം.",
        badge="ഭരണി മാസ്റ്റർ",
        story=["മിടുക്കരായ കുട്ടികൾ പോക്കറ്റ് മണി മൂന്ന് ഭരണിയായി ഭാഗിക്കും: സമ്പാദ്യം, ചെലവ്, പങ്കുവെക്കൽ.",
               "സമ്പാദ്യം വലിയ ലക്ഷ്യങ്ങൾക്കാ. ചെലവ് ഇപ്പോൾ വേണ്ട സാധനങ്ങൾക്കാ. പങ്കുവെക്കൽ മറ്റുള്ളവരെ സഹായിക്കാനാ.",
               "ഇങ്ങനെയേ ഭാഗിക്കാവൂ എന്നൊന്നുമില്ല, പക്ഷേ ഓരോ ഭരണിക്കും കുറച്ചെങ്കിലും കിട്ടണം."],
        talk="പോക്കറ്റ് മണി മൂന്ന് ചെറിയ കവറുകളിൽ കൊടുക്കുക, ഓരോ മാസവും വിഭജനം കുട്ടി തീരുമാനിക്കട്ടെ.",
        act=dict(cats=["സമ്പാദ്യം", "ചെലവ്", "പങ്കുവെക്കൽ"]),
    ),
    "e2": dict(
        title="നാരങ്ങവെള്ളക്കട",
        blurb="വില നിശ്ചയിച്ച് ലാഭമുണ്ടോ എന്ന് നോക്കാം.",
        badge="ലാഭ വിദഗ്ധൻ",
        story=["ആശ നാരങ്ങാവെള്ളം വിൽക്കുന്ന ഒരു കട നടത്തുന്നുണ്ട്. ഒരു ഗ്ലാസ് ഉണ്ടാക്കാൻ ₹6 ചെലവാകും.",
               "ചെലവ് കഴിഞ്ഞ് വിൽപ്പനയിൽ നിന്ന് ബാക്കി കിട്ടുന്ന പൈസയാ ലാഭം.",
               "വില വല്ലാതെ കുറഞ്ഞാൽ നഷ്ടം വരും. വല്ലാതെ കൂടിയാൽ വാങ്ങാൻ ആളുണ്ടാകില്ല."],
        talk="വീട്ടിൽ ഒരു ചെറിയ വിൽപ്പന ആസൂത്രണം ചെയ്യുക, ഉദാഹരണത്തിന് നാരങ്ങവെള്ളം അല്ലെങ്കിൽ പുസ്തക കൈമാറ്റം, ചെലവും ലാഭവും ഒരുമിച്ച് കണക്കാക്കുക.",
        act=dict(product="നാരങ്ങവെള്ളം", unit="ഗ്ലാസ്", days=["സാധാരണ ദിവസം", "ചൂടുള്ള ദിവസം", "മഴയുള്ള ദിവസം"]),
    ),
    "e3": dict(
        title="സുരക്ഷിത പണം, തട്ടിപ്പ് ജാഗ്രത",
        blurb="തട്ടിപ്പുകൾ തിരിച്ചറിഞ്ഞ് പണം സുരക്ഷിതമായി സൂക്ഷിക്കാം.",
        badge="തട്ടിപ്പ് പിടിക്കുന്നവൻ",
        story=["ഡിജിറ്റൽ പൈസ നല്ല ഉപകാരമാ, പക്ഷേ പറ്റിക്കാൻ നോക്കുന്നവരും ഉണ്ട്.",
               "നിന്റെ യുപിഐ പിന്നും ഒടിപിയും രഹസ്യമാ. ഒരു ബാങ്കും കടയും അത് ഒരിക്കലും ചോദിക്കില്ല.",
               "എന്തെങ്കിലും പന്തികേട് തോന്നിയാൽ നിർത്തിയിട്ട് വിശ്വാസമുള്ള ഒരു വലിയ ആളോട് പറയണം."],
        talk="അടുത്തിടെ വന്ന ഒരു തട്ടിപ്പ് സന്ദേശം ഒരുമിച്ച് വായിച്ച് ചതിക്കുന്ന വിദ്യകൾ കണ്ടെത്തുക: തിടുക്കം, സമ്മാനങ്ങൾ, രഹസ്യങ്ങൾ ചോദിക്കൽ.",
        act=dict(labels=["സുരക്ഷിതം", "തട്ടിപ്പ് മുന്നറിയിപ്പ്"], items=[
            ("ഗെയിം ചാറ്റിലെ ഒരു അപരിചിതൻ അച്ഛനമ്മമാരുടെ കാർഡ് നമ്പർ ചോദിക്കുന്നു", "അപരിചിതരോട് കാർഡ് വിവരം ഒരിക്കലും പറയരുത്."),
            ("അമ്മ കടയിലെ ക്യുആർ കോഡ് സ്കാൻ ചെയ്ത് പൈസ അടയ്ക്കുമ്പോൾ നീ അടുത്ത് നിൽക്കുന്നു", "വിശ്വാസമുള്ള വലിയ ഒരാളുടെ കൂടെ ശരിക്കുള്ള കടയിൽ പൈസ അടയ്ക്കുന്നത് സേഫാ."),
            ("“നിനക്ക് ഫോൺ സമ്മാനം കിട്ടി! ഇപ്പോൾ ക്ലിക്ക് ചെയ്യൂ!” എന്ന് ഒരു ലിങ്ക്", "ക്ലിക്ക് ചെയ്യണം എന്ന് പറയുന്ന ഫ്രീ സമ്മാനം മിക്കവാറും തട്ടിപ്പാ."),
            ("അച്ഛനമ്മമാരുടെ കൂടെ ബാങ്ക് അക്കൗണ്ടിൽ സമ്പാദ്യം സൂക്ഷിക്കുന്നു", "അച്ഛനമ്മമാരുടെ കൂടെയുള്ള ബാങ്ക് അക്കൗണ്ട് സേഫായ സ്ഥലമാ."),
            ("ഒരാൾ ഫോണിൽ വിളിച്ച് “ഞാൻ ബാങ്കിൽ നിന്നാ, ഒടിപി പറയൂ” എന്ന് പറയുന്നു", "ബാങ്ക് ഒരിക്കലും ഒടിപി ചോദിക്കില്ല."),
            ("ഓൺലൈനിൽ ആരെങ്കിലും പൈസ ചോദിച്ചാൽ അച്ഛനമ്മമാരോട് പറയുന്നു", "വിശ്വാസമുള്ള വലിയ ആളോട് പറയുന്നത് എപ്പോഴും മിടുക്കാ.")]),
    ),
    "e4": dict(
        title="ബജറ്റ് ബോസ്",
        blurb="ഒരു മാസത്തെ പണം ആസൂത്രണം ചെയ്ത് ആവശ്യങ്ങൾക്ക് മുൻഗണന കൊടുക്കാം.",
        badge="ബജറ്റ് ബോസ്",
        story=["നിന്റെ പൈസ എവിടെ പോകണം എന്ന് പറയുന്ന പ്ലാനാ ബജറ്റ്.",
               "ആദ്യം ആവശ്യങ്ങൾ. പിന്നെ സമ്പാദ്യം. അതും കഴിഞ്ഞ് വിനോദം.",
               "വരവും ചെലവും എഴുതിവെച്ചാൽ പൈസ എങ്ങോട്ടാ പോകുന്നത് എന്ന് കാണാം."],
        talk="ഒരു മാസത്തെ പോക്കറ്റ് മണി കടലാസിൽ ആസൂത്രണം ചെയ്യാൻ പറയുക, മാസാവസാനം പരിശോധിക്കുക.",
        act=dict(cats=["സ്കൂൾ സാധനങ്ങൾ", "പലഹാരങ്ങൾ", "വിനോദം", "സമ്പാദ്യം"]),
    ),
    "e5": dict(
        title="ബാങ്കും സമ്പാദ്യവും",
        blurb="ബാങ്ക് എന്താണ് ചെയ്യുന്നതെന്നും പലിശ എന്തിനാണെന്നും അറിയാം.",
        badge="ബാങ്ക് കൂട്ടുകാരൻ",
        story=["ബാങ്ക് നമ്മുടെ പൈസ സേഫായി സൂക്ഷിക്കും, വേറെ ആളുകൾക്ക് ലോൺ കൊടുക്കുകയും ചെയ്യും.",
               "സേവിങ്സ് അക്കൗണ്ടിൽ പൈസ ഇട്ടാൽ ബാങ്ക് ഒരു ചെറിയ പലിശ തരും.",
               "കുട്ടികൾ അക്കൗണ്ട് തുടങ്ങുന്നത് അച്ഛനമ്മമാരുടെയോ രക്ഷിതാവിന്റെയോ കൂടെയാ."],
        talk="ഒരുമിച്ച് ബാങ്ക് ശാഖ സന്ദർശിക്കുകയോ ബാങ്ക് ആപ്പ് തുറക്കുകയോ ചെയ്ത് ഒരു സ്റ്റേറ്റ്മെന്റ് വരി വരിയായി വായിക്കുക.",
        act=dict(labels=["ബാങ്ക് ചെയ്യുന്നത്", "ബാങ്ക് ചെയ്യാത്തത്"], items=[
            ("നിന്റെ സമ്പാദ്യം സേഫായി സൂക്ഷിക്കുന്നു", "സേഫായി സൂക്ഷിക്കലാ ബാങ്കിന്റെ പ്രധാന പണി."),
            ("സമ്പാദ്യത്തിന് പലിശ തരുന്നു", "പലിശ സമ്പാദിക്കുന്നവർക്കുള്ള പ്രതിഫലമാ."),
            ("പലിശ വാങ്ങി പൈസ ലോൺ കൊടുക്കുന്നു", "ലോൺ കൊടുത്തിട്ടാ ബാങ്കിന് വരുമാനം കിട്ടുന്നത്."),
            ("ഐസ്ക്രീം വിൽക്കുന്നു", "അത് ഒരു കടയുടെ പണിയാ."),
            ("സൈക്കിൾ നന്നാക്കുന്നു", "അത് മെക്കാനിക്കിന്റെ പണിയാ."),
            ("പാസ്ബുക്കോ സ്റ്റേറ്റ്മെന്റോ തരുന്നു", "പൈസ വരുന്നതും പോകുന്നതും അതിൽ എഴുതും.")]),
    ),
    "e6": dict(
        title="യുപിഐയും ഡിജിറ്റൽ പേയ്മെന്റും",
        blurb="സുരക്ഷിതമായി പണം അടയ്ക്കാൻ പടിപടിയായി പഠിക്കാം.",
        badge="യുപിഐ കാവൽ",
        story=["ഫോൺ ഉപയോഗിച്ച് പെട്ടെന്ന് പൈസ അടയ്ക്കാൻ യുപിഐ സഹായിക്കും.",
               "പൈസ അയക്കുമ്പോൾ മാത്രമേ പിൻ വേണ്ടൂ. പൈസ കിട്ടാൻ ആർക്കും നിന്റെ പിൻ വേണ്ട.",
               "പൈസ അടയ്ക്കുന്നതിന് മുൻപ് പേരും തുകയും എപ്പോഴും നോക്കണം."],
        talk="അടുത്ത തവണ യുപിഐ വഴി പണം അടയ്ക്കുമ്പോൾ ഓരോ സുരക്ഷാ ഘട്ടവും ഉറക്കെ പറയുക.",
        act=dict(title="കടയിൽ സേഫായി പൈസ അടയ്ക്കുന്ന സ്റ്റെപ്പുകൾ ക്രമത്തിൽ വെക്കൂ", steps=[
            "അടയ്ക്കേണ്ട തുക നോക്കുക",
            "അച്ഛനമ്മമാരുടെ കൂടെ കടയിലെ ക്യുആർ കോഡ് സ്കാൻ ചെയ്യുക",
            "കാണിക്കുന്ന കടയുടെ പേര് ശരിയാണോ എന്ന് നോക്കുക",
            "അച്ഛനമ്മമാർ പിൻ അടിക്കുക",
            "സക്സസ് മെസ്സേജ് വരുന്നത് വരെ കാത്തിരിക്കുക"]),
    ),
    "e7": dict(
        title="ലക്ഷ്യങ്ങളും സ്വപ്നങ്ങളും",
        blurb="വലിയ ലക്ഷ്യത്തെ ആഴ്ചതോറുമുള്ള ചെറിയ ഘട്ടങ്ങളാക്കാം.",
        badge="ലക്ഷ്യം നേടുന്നവൻ",
        story=["എന്താ വേണ്ടത്, എത്ര രൂപ ആകും, എപ്പോഴത്തേക്ക് വേണം എന്ന് പറയുന്നതാ ലക്ഷ്യം.",
               "വലിയ ലക്ഷ്യം ആഴ്ച തോറുമുള്ള ചെറിയ സ്റ്റെപ്പുകളായി ഭാഗിച്ചാൽ എളുപ്പമാകും.",
               "ലക്ഷ്യത്തിൽ എത്തുമ്പോൾ നല്ല സന്തോഷം തോന്നും, ഒപ്പം നല്ലൊരു ശീലവും കിട്ടും."],
        talk="ഒരു ലക്ഷ്യം, അതിന്റെ വിലയും തീയതിയും സഹിതം, ഫ്രിഡ്ജിൽ എഴുതി ഒട്ടിച്ച് ആഴ്ചതോറും പുരോഗതി നോക്കുക.",
        act=dict(unit="ആഴ്ച", unit_pl="ആഴ്ച", what="ഫുട്ബോൾ"),
    ),

    # ------------------------------------------------------------- Pioneers
    "p1": dict(
        title="കൂട്ടുപലിശയുടെ മാജിക്",
        blurb="പലിശയ്ക്ക് പലിശ കിട്ടുമ്പോൾ ചെറിയ സമ്പാദ്യം വളരുന്നത് കാണാം.",
        badge="കൂട്ടുപലിശ മാന്ത്രികൻ",
        story=["നിന്റെ സമ്പാദ്യത്തിന് പലിശ കിട്ടും, ആ പലിശയ്ക്കും പലിശ കിട്ടും. അതിനെയാ കൂട്ടുപലിശ എന്ന് പറയുന്നത്.",
               "ഏറ്റവും പ്രധാനം സമയമാ. നേരത്തെ തുടങ്ങിയാൽ പൈസയ്ക്ക് കൂടുതൽ കാലം വളരാം.",
               "ഈ ഗെയിമിലെ നിരക്കുകൾ വെറും ഉദാഹരണമാ, ഉറപ്പൊന്നുമല്ല. ശരിക്കുള്ള ആദായം മാറിക്കൊണ്ടിരിക്കും."],
        talk="ഒരു റിക്കറിങ് ഡെപ്പോസിറ്റ് അല്ലെങ്കിൽ എസ്ഐപി കാൽക്കുലേറ്റർ തുറന്ന് ഒരേ പ്രതിമാസ തുക 5 വർഷത്തേക്കും 15 വർഷത്തേക്കും താരതമ്യം ചെയ്യുക.",
    ),
    "p2": dict(
        title="പ്രാക്ടീസ് മാർക്കറ്റ്",
        blurb="സാങ്കൽപ്പിക കമ്പനികളിൽ പരിശീലന പണം ഭാഗിച്ച് നോക്കാം.",
        badge="റിസ്ക് അന്വേഷകൻ",
        story=["ഒരു കമ്പനിയുടെ ചെറിയ ഒരു ഭാഗത്തിന്റെ ഉടമസ്ഥതയാ ഓഹരി (ഷെയർ).",
               "ഷെയറിന്റെ വില കൂടുകയും കുറയുകയും ചെയ്യും. ചില കമ്പനികളുടെ വില മറ്റുള്ളവയെക്കാൾ കൂടുതൽ മേലോട്ടും താഴോട്ടും പോകും.",
               "പൈസ പല സ്ഥലത്തായി ഭാഗിച്ച് ഇടുന്നതിനെ ഡൈവേഴ്സിഫിക്കേഷൻ എന്ന് പറയും. അത് യാത്ര എളുപ്പമാക്കും. ഈ കമ്പനികൾ ഭാവനയിലുള്ളതാ, പൈസ വെറും പ്രാക്ടീസ് പൈസയാ."],
        talk="നിങ്ങളുടെ കുടുംബം ഉപയോഗിക്കുന്ന മൂന്ന് ബ്രാൻഡുകൾ തിരഞ്ഞെടുത്ത് ഒരു ബിസിനസ് ശക്തമാകുന്നത് എന്തുകൊണ്ടാണെന്ന് സംസാരിക്കുക. ഒന്നും വാങ്ങരുത്.",
    ),
    "p3": dict(
        title="₹100 കൊണ്ട് കുറച്ചേ കിട്ടുന്നത് എന്തുകൊണ്ട്",
        blurb="വെറുതെ വെച്ച പണത്തിന്റെ മൂല്യം വിലക്കയറ്റം കുറയ്ക്കുന്നത് കാണാം.",
        badge="വിലക്കയറ്റ പോരാളി",
        story=["കാലം കഴിയുംതോറും വില കൂടുന്നതിനെയാ വിലക്കയറ്റം (ഇൻഫ്ലേഷൻ) എന്ന് പറയുന്നത്.",
               "ഇന്ന് ₹100 വിലയുള്ള ഒരു പലഹാരത്തിന് പിന്നീട് കൂടുതൽ വില വരും.",
               "അതുകൊണ്ട് അലമാരയിൽ വെറുതെ ഇരിക്കുന്ന പൈസയ്ക്ക് ഓരോ വർഷവും വാങ്ങൽ ശേഷി കുറയും. വിലക്കയറ്റത്തിനൊപ്പം എത്താൻ പൈസയ്ക്ക് ഒരു പ്ലാൻ വേണം."],
        talk="അവർ ചെറുപ്പമായിരുന്നപ്പോൾ ഒരു ചായയ്ക്കോ സിനിമാ ടിക്കറ്റിനോ എത്ര വിലയായിരുന്നു എന്ന് മുത്തശ്ശീമുത്തശ്ശന്മാരോട് ചോദിക്കുക.",
    ),
    "p4": dict(
        title="ഓഹരി, ഫണ്ട്, എഫ്ഡി, സ്വർണം",
        blurb="ഓരോ തരം നിക്ഷേപവും എന്താണെന്ന് പഠിക്കാം.",
        badge="സ്മാർട്ട് മിക്സർ",
        story=["പൈസ പണിയെടുപ്പിക്കാൻ പല വഴികളുണ്ട്: ഷെയർ, മ്യൂച്വൽ ഫണ്ട്, സ്ഥിര നിക്ഷേപം, സ്വർണം.",
               "ഓരോന്നിലും റിസ്കും നേട്ടവും വ്യത്യസ്തമായ അളവിലാ.",
               "ഈ ഗെയിം ആശയങ്ങൾ മാത്രമേ പഠിപ്പിക്കുന്നുള്ളൂ. എന്ത് വാങ്ങണം എന്ന് ഇത് ആരോടും പറയുന്നില്ല."],
        talk="ഒരു ഓഹരിയും ഒരു എഫ്ഡിയും തമ്മിലുള്ള വ്യത്യാസം സ്വന്തം വാക്കുകളിൽ വിശദീകരിക്കാൻ കുട്ടിയോട് പറയുക.",
        act=dict(labels=["ഓഹരി", "മ്യൂച്വൽ ഫണ്ട്", "സ്ഥിര നിക്ഷേപം", "സ്വർണം"], items=[
            ("ഒരു കമ്പനിയുടെ ചെറിയൊരു ഭാഗം നിനക്ക് സ്വന്തമാണ്", "അത് ഷെയറാ."),
            ("പലരും പൈസ ഒരുമിച്ച് ചേർക്കുന്നു, വിദഗ്ധനായ ഫണ്ട് മാനേജർ അത് നിക്ഷേപിക്കുന്നു", "അത് മ്യൂച്വൽ ഫണ്ടാ."),
            ("കുറച്ച് കാലത്തേക്ക് ഉറപ്പിച്ച നിരക്കിൽ ബാങ്കിന് പൈസ കടം കൊടുക്കുന്നു", "അത് സ്ഥിര നിക്ഷേപമാ."),
            ("ദീർഘകാലത്തേക്ക് ആളുകൾ സൂക്ഷിക്കുന്ന നാണയങ്ങളോ ആഭരണങ്ങളോ", "അത് സ്വർണമാ."),
            ("വില വല്ലാതെ കയറിയിറങ്ങാം, ഡിവിഡന്റ് തരുകയും ചെയ്യാം", "ഷെയറിന്റെ വില കയറിയിറങ്ങും, ഡിവിഡന്റ് തന്നെന്നും വരാം."),
            ("തീരും വരെ വെച്ചാൽ ആദായം മുൻകൂട്ടി അറിയാം", "സ്ഥിര നിക്ഷേപത്തിൽ നിരക്ക് തുടക്കത്തിൽ തന്നെ പറയും.")]),
    ),
    "p5": dict(
        title="ക്രെഡിറ്റ്, വായ്പ, കടം",
        blurb="ഒരു വായ്പയ്ക്ക് യഥാർത്ഥത്തിൽ എത്ര ചെലവാകുമെന്ന് കാണാം.",
        badge="കടക്കെണി ഒഴിവാക്കുന്നവൻ",
        story=["പലിശ സഹിതം തിരിച്ചടയ്ക്കേണ്ട, കടം വാങ്ങിയ പൈസയാ ലോൺ.",
               "കാലാവധി കൂടിയ ലോണിൽ മാസത്തെ അടവ് കുറവായിരിക്കും, പക്ഷേ ആകെ പലിശ കൂടുതലായിരിക്കും.",
               "ആവശ്യങ്ങൾക്ക് മാത്രം, പ്ലാനോടെ, വിശ്വസിക്കാവുന്നതും നിയമപ്രകാരം പ്രവർത്തിക്കുന്നതുമായ സ്ഥാപനങ്ങളിൽ നിന്ന് മാത്രം കടം വാങ്ങുക."],
        talk="ഒരു യഥാർത്ഥ ഇഎംഐ ഓഫർ ഒരുമിച്ച് നോക്കി ആകെ അടയ്ക്കേണ്ട തുക കണക്കാക്കുക.",
    ),
    "p6": dict(
        title="നികുതിയും ശമ്പളവും",
        blurb="ഒരു ശമ്പളത്തിന് എന്ത് സംഭവിക്കുന്നു എന്ന് മനസ്സിലാക്കാം.",
        badge="നികുതി വിദഗ്ധൻ",
        story=["നീ എത്ര സമ്പാദിക്കുന്നു, എന്തൊക്കെ കുറയുന്നു എന്ന് പേസ്ലിപ്പ് കാണിച്ചു തരും.",
               "റോഡ്, സ്കൂൾ, ആശുപത്രി തുടങ്ങിയവയുടെ ചെലവിന് നികുതി സഹായിക്കും.",
               "ഗ്രോസ് ശമ്പളവും നെറ്റ് ശമ്പളവും അറിഞ്ഞാൽ പ്ലാൻ ചെയ്യാൻ എളുപ്പമാകും."],
        talk="ജിഎസ്ടിയുള്ള ഒരു ബിൽ കുട്ടിയെ കാണിച്ച് നികുതി വരി ചൂണ്ടിക്കാണിക്കുക.",
        act=dict(labels=["വരുന്നത്", "പോകുന്നത്"], items=[
            ("ശമ്പളം അക്കൗണ്ടിൽ വരുന്നു", "വരുമാനം വരുന്നു."),
            ("ആദായനികുതി അടയ്ക്കുന്നു", "നികുതി പുറത്തേക്ക് പോകുന്നു."),
            ("പ്രതിമാസ വാടക", "വാടക പുറത്തേക്ക് പോകുന്നു."),
            ("ജോലിയിൽ നിന്നുള്ള ബോണസ്", "ബോണസ് വരുന്നു."),
            ("സമ്പാദ്യത്തിന് കിട്ടുന്ന പലിശ", "പലിശ വരുന്നു."),
            ("വൈദ്യുതി ബിൽ", "ബില്ല് പുറത്തേക്ക് പോകുന്നു.")]),
    ),
    "p7": dict(
        title="ഒരു ചെറിയ ബിസിനസ് തുടങ്ങാം",
        blurb="കൈകൊണ്ട് ഉണ്ടാക്കിയ മെഴുകുതിരികൾക്ക് വില നിശ്ചയിച്ച് മാർജിൻ പഠിക്കാം.",
        badge="യുവ സ്ഥാപകൻ",
        story=["ഒരു പ്രശ്നം പരിഹരിക്കാൻ ബിസിനസ് തുടങ്ങുന്ന ആളാ സംരംഭകൻ.",
               "വരുമാനത്തിൽ നിന്ന് ചെലവ് കുറച്ചാൽ ലാഭം. ചില ചെലവുകൾ മാറില്ല, ചിലത് ഓരോ സാധനത്തിനും മാറും.",
               "വില, ക്വാളിറ്റി, കസ്റ്റമേഴ്സ് ഇവയാ വിജയം തീരുമാനിക്കുന്നത്."],
        talk="ഒരു ദിവസത്തേക്ക് കുട്ടിക്ക് നടത്താവുന്ന ചെറിയ ബിസിനസ് ആലോചിച്ച് അതിന്റെ ചെലവുകൾ പട്ടികപ്പെടുത്തുക.",
        act=dict(product="കൈകൊണ്ട് ഉണ്ടാക്കിയ മെഴുകുതിരി", unit="മെഴുകുതിരി",
                 days=["സാധാരണ ആഴ്ച", "ഉത്സവ ആഴ്ച", "തിരക്കില്ലാത്ത ആഴ്ച"]),
    ),
    "p8": dict(
        title="ഓൺലൈൻ തട്ടിപ്പും സൈബർ സുരക്ഷയും",
        blurb="ആധുനിക തട്ടിപ്പുകൾ തിരിച്ചറിഞ്ഞ് ഓൺലൈനിൽ സുരക്ഷിതരാകാം.",
        badge="സൈബർ കവചം",
        story=["തട്ടിപ്പുകാർ ആളുകളെ തിടുക്കം കൂട്ടിച്ചും പേടിപ്പിച്ചും രഹസ്യം പറയിപ്പിക്കാൻ നോക്കും.",
               "ധൃതി വേണ്ട, പതുക്കെ ചെയ്യുക. ഒഫീഷ്യൽ ആപ്പും നമ്പറും ഉപയോഗിച്ച് ഉറപ്പ് വരുത്തുക.",
               "എന്തെങ്കിലും കുഴപ്പം പറ്റിയാൽ വിശ്വാസമുള്ള ഒരു വലിയ ആളോട് പറയുക, വേഗം റിപ്പോർട്ട് ചെയ്യുകയും ചെയ്യുക."],
        talk="ദേശീയ സൈബർ ക്രൈം ഹെൽപ്പ്‌ലൈൻ നമ്പർ 1930 വീട്ടിലെ ഫോണിൽ സേവ് ചെയ്യുക.",
        act=dict(labels=["സുരക്ഷിതം", "തട്ടിപ്പ് മുന്നറിയിപ്പ്"], items=[
            ("“നീ ഡിജിറ്റൽ അറസ്റ്റിലാ, പൈസ അടയ്ക്കണം” എന്ന് ഒരാൾ ഫോണിൽ പറയുന്നു", "ശരിക്കുള്ള പോലീസ് ഫോൺ വിളിച്ച് പൈസ ചോദിക്കില്ല."),
            ("ബാങ്കിന്റെ ഒഫീഷ്യൽ ആപ്പിൽ ബാലൻസ് നോക്കുന്നു", "ഒഫീഷ്യൽ ആപ്പുകൾ സേഫാ."),
            ("“ഇന്ന് തന്നെ കെവൈസി അപ്ഡേറ്റ് ചെയ്തില്ലെങ്കിൽ അക്കൗണ്ട് ക്ലോസ് ആകും” എന്ന് ഒരു ലിങ്ക്", "ധൃതി കൂട്ടലും ലിങ്കും ചേർന്നാൽ അത് തട്ടിപ്പാ."),
            ("ടു-ഫാക്ടർ ലോഗിൻ ഓൺ ചെയ്യുന്നു", "അത് നിന്റെ അക്കൗണ്ടുകളെ സംരക്ഷിക്കും."),
            ("അറിയാത്ത സൈറ്റിലെ 90% ഓഫറുള്ള ഫോൺ", "വിശ്വസിക്കാൻ പറ്റാത്തത്ര നല്ലത്, തട്ടിപ്പാകും."),
            ("പുതിയ ആപ്പ് ഇൻസ്റ്റാൾ ചെയ്യുന്നതിന് മുൻപ് അച്ഛനമ്മമാരോട് ചോദിക്കുന്നു", "വേറൊരാളോട് അഭിപ്രായം ചോദിക്കുന്നത് മിടുക്കാ.")]),
    ),
}
'''

_SOURCES['ml_bank_seed'] = r'''"""Malayalam question bank for Seedlings (s1 to s7), in spoken Kerala Malayalam. Same order and option count as content.py."""

BANK = {
"s1": [
    ("ഏറ്റവും വില കൂടുതൽ ഏതിനാ?", ["₹2 നാണയം", "₹5 നാണയം", "₹10 നോട്ട്"], "10 ആണ് 5 നെക്കാളും 2 നെക്കാളും വലുത്."),
    ("₹5 ആകാൻ എത്ര ₹1 നാണയം വേണം?", ["2", "5", "10"], "അഞ്ച് ഒന്ന് കൂട്ടിയാൽ അഞ്ചാകും."),
    ("₹3 ന്റെ മിഠായിക്ക് നീ ₹10 കൊടുത്തു. കടക്കാരൻ എത്ര തിരിച്ചു തരും?", ["₹3", "₹7", "₹10"], "10 ൽ നിന്ന് 3 പോയാൽ 7 ബാക്കി."),
    ("ഇതിൽ ഏറ്റവും വലിയ സംഖ്യ ഏതാ?", ["₹5", "₹20", "₹10"], "20 ആണ് 10 നെക്കാളും 5 നെക്കാളും വലുത്."),
    ("പൈസ സൂക്ഷിക്കാൻ പറ്റിയ സ്ഥലം ഏതാ?", ["വീട്ടിലെ കുടുക്കയിൽ", "ബസ് സീറ്റിൽ", "ഒരു അപരിചിതന്റെ കൈയിൽ"], "വീട്ടിലെ കുടുക്കയിൽ ഇട്ടാൽ പൈസ സേഫാ."),
    ("ഒരു ബിസ്കറ്റ് വാങ്ങാൻ കടക്കാരന് എന്താ കൊടുക്കുക?", ["പൈസ", "ഇലകൾ", "കല്ലുകൾ"], "കടയിൽ പൈസ കൊടുത്താലേ സാധനം കിട്ടൂ."),
    ("രണ്ട് ₹5 നാണയം കൂടിയാൽ എത്ര ആകും?", ["₹7", "₹10", "₹52"], "5 ഉം 5 ഉം കൂടിയാൽ 10."),
    ("ഇതിൽ കടലാസ് കൊണ്ട് ഉണ്ടാക്കിയത് ഏതാ?", ["ഒരു നോട്ട്", "ഒരു നാണയം", "ഒരു താക്കോൽ"], "നോട്ട് കടലാസ് പൈസയാ."),
    ("₹5 + ₹5 + ₹1 = ?", ["₹10", "₹11", "₹55"], "10 ന്റെ കൂടെ 1 കൂടി കൂട്ടിയാൽ 11."),
    ("ഒരു പെൻസിലിന് ₹6 ആണ്. നിന്റെ കൈയിൽ ₹5 ഉണ്ട്. ഇനി എത്ര വേണം?", ["₹1 കൂടി", "₹5 കൂടി", "ഒന്നും വേണ്ട"], "6 ൽ നിന്ന് 5 പോയാൽ 1 ബാക്കി."),
    ("ഏതിലാ ഏറ്റവും കൂടുതൽ പൈസ ഉള്ളത്?", ["മൂന്ന് ₹1 നാണയം", "ഒരു ₹5 നാണയം", "രണ്ട് ₹1 നാണയം"], "5 ആണ് 3 നെക്കാളും 2 നെക്കാളും വലുത്."),
    ("വഴിയിൽ നിന്ന് ഒരു നാണയം കിട്ടി. നീ എന്ത് ചെയ്യണം?", ["വലിയ ഒരാളോട് പറയണം", "എടുത്ത് എറിയണം", "ഒളിപ്പിച്ച് വെക്കണം"], "വലിയവർക്ക് സഹായിക്കാൻ പറ്റും."),
],
"s2": [
    ("ഇതിൽ ആവശ്യമുള്ള സാധനം ഏതാ?", ["ചോക്ലേറ്റ്", "ചൂടുള്ള ചോറ്", "കളിപ്പാട്ട റോബോട്ട്"], "ഭക്ഷണം കഴിച്ചാലേ നമ്മൾ ആരോഗ്യത്തോടെ ഇരിക്കൂ."),
    ("നിനക്ക് പുതിയ കളിപ്പാട്ടവും വേണം, സ്കൂൾ പുസ്തകവും വേണം. ആദ്യം എന്ത് വാങ്ങും?", ["കളിപ്പാട്ടം", "സ്കൂൾ പുസ്തകം", "രണ്ടും എപ്പോഴും"], "ആവശ്യങ്ങൾ ആദ്യം. കളിപ്പാട്ടം കുറച്ച് കഴിഞ്ഞ് മതി."),
    ("ആഗ്രഹമുള്ള സാധനം വാങ്ങുന്നത് തെറ്റാണോ?", ["അതെ, ഒരിക്കലും പാടില്ല", "അല്ല, ആവശ്യങ്ങൾ കഴിഞ്ഞ്, സമ്പാദിച്ചിട്ട് വാങ്ങാം", "ഞായറാഴ്ച മാത്രം"], "പ്ലാൻ ചെയ്ത് വാങ്ങിയാൽ ആഗ്രഹങ്ങളും വാങ്ങാം."),
    ("ഇതിൽ ആഗ്രഹം ഏതാ?", ["വെള്ളം", "മരുന്ന്", "വീഡിയോ ഗെയിം"], "വീഡിയോ ഗെയിം ഇല്ലെങ്കിലും നമുക്ക് ജീവിക്കാം."),
    ("ജീവിക്കാൻ നമുക്ക് ദിവസവും വേണ്ടത് എന്താ?", ["ഭക്ഷണവും വെള്ളവും", "ബലൂൺ", "സ്റ്റിക്കർ"], "ഭക്ഷണവും വെള്ളവും ഉണ്ടെങ്കിലേ ശരീരം പണിയെടുക്കൂ."),
    ("ഐസ്ക്രീം ഒരു...", ["ആവശ്യം", "ആഗ്രഹം", "മരുന്ന്"], "അത് രുചിക്ക് വേണ്ടി കഴിക്കുന്നതാ."),
    ("സ്കൂൾ പുസ്തകവും സ്കൂൾ ബാഗും...", ["പഠിക്കാൻ വേണ്ട ആവശ്യങ്ങൾ", "വെറും ആഗ്രഹങ്ങൾ", "ഒരു ഉപയോഗവും ഇല്ലാത്തത്"], "പഠിക്കാൻ അതൊക്കെ വേണം."),
    ("ഒരു ആഗ്രഹം വാങ്ങുന്നതിന് മുൻപ് എന്താ നോക്കേണ്ടത്?", ["ആവശ്യങ്ങൾ കഴിഞ്ഞ് പൈസ ബാക്കിയുണ്ടോ എന്ന്", "കൂട്ടുകാർക്ക് ഉണ്ടോ എന്ന്", "ഓഫർ ഉണ്ടോ എന്ന്"], "ആദ്യം ആവശ്യങ്ങൾക്കാ പൈസ കൊടുക്കേണ്ടത്."),
    ("അസുഖം വരുമ്പോൾ കഴിക്കുന്ന മരുന്ന് ഒരു...", ["ആവശ്യം", "ആഗ്രഹം", "കളിപ്പാട്ടം"], "അസുഖം മാറാൻ അത് വേണം."),
    ("ഒരു കളിപ്പാട്ട കാർ ഒരു...", ["ആവശ്യം", "ആഗ്രഹം", "ഭക്ഷണം"], "കളിപ്പാട്ടം രസമാ, പക്ഷേ അത്യാവശ്യമൊന്നുമല്ല."),
    ("ഏത് ജോഡിയിലാ രണ്ടും ആവശ്യങ്ങൾ?", ["ഭക്ഷണവും വെള്ളവും", "കളിപ്പാട്ടവും മിഠായിയും", "ഗെയിമും ബലൂണും"], "രണ്ടും ഉണ്ടെങ്കിലേ നമ്മൾ ആരോഗ്യത്തോടെ ജീവിക്കൂ."),
    ("പൈസ കുറവാ. ആദ്യം എന്ത് വാങ്ങണം?", ["രാത്രിക്ക് വേണ്ട അരി", "ഒരു സ്റ്റിക്കർ", "ഒരു കളിപ്പാട്ടം"], "ഭക്ഷണം ഒരു ആവശ്യമാണല്ലോ."),
],
"s3": [
    ("പിങ്കു ദിവസവും ₹5 വീതം സമ്പാദിക്കും. ₹30 ആകാൻ എത്ര ദിവസം വേണം?", ["4 ദിവസം", "6 ദിവസം", "10 ദിവസം"], "5 നെ 6 പ്രാവശ്യം കൂട്ടിയാൽ 30."),
    ("മീര എന്നും മിഠായി വാങ്ങും. പിങ്കു സമ്പാദിക്കും. ആർക്കാ കളിപ്പാട്ട സൈക്കിൾ ആദ്യം കിട്ടുക?", ["മീരയ്ക്ക്", "പിങ്കുവിന്", "രണ്ടാൾക്കും ഒരേ ദിവസം"], "സമ്പാദിച്ചാൽ ലക്ഷ്യത്തിലേക്ക് അടുക്കും."),
    ("സമ്പാദിക്കുക എന്നാൽ...", ["ഇന്ന് തന്നെ മുഴുവൻ ചെലവാക്കുക", "കുറച്ച് പൈസ പിന്നത്തേക്ക് മാറ്റിവെക്കുക", "എല്ലാവരിൽ നിന്നും ഒളിപ്പിക്കുക"], "കുറച്ച് പിന്നത്തേക്ക് മാറ്റിവെക്കുന്നതാണ് സമ്പാദ്യം."),
    ("സമ്പാദ്യം സൂക്ഷിക്കാൻ നല്ല സ്ഥലം ഏതാ?", ["വീട്ടിലെ കുടുക്ക", "തുറന്ന പോക്കറ്റ്", "അപരിചിതന്റെ കൈ"], "വീട്ടിലെ കുടുക്കയിൽ പൈസ സേഫാ."),
    ("ദിവസവും ₹2 വീതം 5 ദിവസം സമ്പാദിച്ചാൽ എത്ര കിട്ടും?", ["₹7", "₹10", "₹25"], "2 നെ 5 പ്രാവശ്യം കൂട്ടിയാൽ 10."),
    ("വലിയ ലക്ഷ്യത്തിൽ എത്താൻ എന്താ സഹായിക്കുക?", ["ക്ഷമ", "പെട്ടെന്ന് ചെലവാക്കൽ", "നാണയം കളയൽ"], "ചെറിയ ചെറിയ ചുവടുകൾ കൂടി വലിയ ലക്ഷ്യത്തിൽ എത്തും."),
    ("നിന്റെ കുടുക്കയിൽ ₹20 ഉണ്ട്. കളിപ്പാട്ടത്തിന് ₹50 ആണ്. ഇനി എത്ര വേണം?", ["₹20", "₹30", "₹70"], "50 ൽ നിന്ന് 20 പോയാൽ 30."),
    ("കുറേ ചെറിയ നാണയങ്ങൾ ഒരുമിച്ച് കൂട്ടിയാൽ...", ["കുറേ പൈസ ആകും", "ഒന്നും ഉണ്ടാകില്ല", "പൈസ കുറഞ്ഞുപോകും"], "ചെറിയ തുകകൾ കൂടിക്കൂടി വലുതാകും."),
    ("ആഴ്ചയിൽ ₹10 വീതം സമ്പാദിച്ചാൽ 4 ആഴ്ച കഴിയുമ്പോൾ എത്ര ആകും?", ["₹14", "₹40", "₹100"], "10 നെ 4 പ്രാവശ്യം കൂട്ടിയാൽ 40."),
    ("സമ്പാദിച്ച് തുടങ്ങാൻ പറ്റിയ സമയം എപ്പോഴാ?", ["ഇന്ന്", "ഒരിക്കലും അല്ല", "വയസ്സായിട്ട്"], "നേരത്തെ തുടങ്ങിയാൽ അതൊരു ശീലമാകും."),
    ("ഇതിൽ സമ്പാദ്യം ഏതാ?", ["₹5 കുടുക്കയിൽ ഇടുന്നത്", "മിഠായി വാങ്ങുന്നത്", "നാണയം കളയുന്നത്"], "പൈസ എടുത്തുവെക്കുന്നതാണ് സമ്പാദിക്കൽ."),
    ("ഒരു കൂട്ടുകാരൻ നിന്റെ സമ്പാദ്യം മുഴുവൻ ചോദിക്കുന്നു. നീ എന്ത് ചെയ്യും?", ["ആദ്യം വിശ്വാസമുള്ള ഒരു വലിയ ആളോട് ചോദിക്കും", "മുഴുവൻ കൊടുക്കും", "ഒളിപ്പിച്ച് വെക്കും"], "വലിയ പൈസക്കാര്യം വലിയവരോട് ചോദിച്ചിട്ടേ തീരുമാനിക്കാവൂ."),
],
"s4": [
    ("പൈസ സാധാരണ എവിടെ നിന്നാ വരുന്നത്?", ["ജോലി ചെയ്തിട്ട്", "മരത്തിൽ നിന്ന്", "ആഗ്രഹിച്ചാൽ മതി"], "ആളുകൾ ജോലി ചെയ്ത് പൈസ ഉണ്ടാക്കുന്നു."),
    ("ഒരു കർഷകൻ പച്ചക്കറി വിൽക്കുന്നു. അത് എന്താ?", ["പൈസ ഉണ്ടാക്കൽ", "ഒരു സമ്മാനം", "പൈസ പോകൽ"], "കൃഷി ചെയ്തത് വിറ്റ് പൈസ ഉണ്ടാക്കുന്നു."),
    ("പൈസ സമ്മാനമായി കിട്ടുക എന്നാൽ എന്താ?", ["ജോലിക്ക് അല്ലാതെ സ്നേഹം കൊണ്ട് തരുന്ന പൈസ", "കടയിൽ നിന്ന് കിട്ടുന്ന പൈസ", "വഴിയിൽ നിന്ന് കിട്ടുന്ന പൈസ"], "സമ്മാനം എന്നാൽ സൗജന്യമായി തരുന്നതാ."),
    ("ഒരു ടീച്ചർ കുട്ടികളെ പഠിപ്പിക്കുന്നു. ടീച്ചർക്ക് പൈസ എങ്ങനെ കിട്ടും?", ["ശമ്പളമായി", "കളിപ്പാട്ടം വിറ്റിട്ട്", "നാണയം കിട്ടിയിട്ട്"], "ജോലി ചെയ്താൽ കിട്ടുന്ന കൂലിയാണ് ശമ്പളം."),
    ("വിഷുക്കൈനീട്ടം എന്നാൽ...", ["വലിയവർ തരുന്ന സമ്മാനപ്പൈസ", "ജോലിക്ക് കിട്ടുന്ന കൂലി", "ബാങ്കിൽ നിന്നുള്ള ലോൺ"], "വലിയവർ അനുഗ്രഹത്തോടെ തരുന്നതാ അത്."),
    ("ഒരു കുട്ടിക്ക് നല്ല രീതിയിൽ കുറച്ച് പൈസ എങ്ങനെ ഉണ്ടാക്കാം?", ["വീട്ടിൽ ഉണ്ടാക്കിയ കാർഡുകൾ അയൽക്കാർക്ക് വിൽക്കാം", "ബാഗിൽ നിന്ന് പൈസ എടുക്കാം", "അപരിചിതരോട് പൈസ ചോദിക്കാം"], "ഉണ്ടാക്കി വിൽക്കുന്നത് നല്ല സത്യസന്ധമായ പണിയാ."),
    ("ഡോക്ടർമാർക്ക് പൈസ കിട്ടുന്നത് എങ്ങനെയാ?", ["രോഗികളെ ചികിത്സിച്ചിട്ട്", "മധുരം വിറ്റിട്ട്", "ബസ് ഓടിച്ചിട്ട്"], "രോഗികളെ സഹായിക്കലാണ് അവരുടെ ജോലി."),
    ("ആളുകൾ എന്തിനാ ജോലി ചെയ്യുന്നത്?", ["ഭക്ഷണത്തിനും ആവശ്യങ്ങൾക്കും വേണ്ട പൈസ ഉണ്ടാക്കാൻ", "വെറുതെ ക്ഷീണിക്കാൻ", "പൈസ കളയാൻ"], "ആവശ്യമുള്ള സാധനങ്ങൾക്ക് പൈസ കൊടുക്കാൻ ജോലി വേണം."),
    ("നീ ₹5 വീതം 2 പെൻസിൽ വിൽക്കുന്നു. എത്ര രൂപ കിട്ടും?", ["₹7", "₹10", "₹25"], "5 നെ 2 പ്രാവശ്യം കൂട്ടിയാൽ 10."),
    ("ബസ് ഡ്രൈവർക്ക് പൈസ കിട്ടുന്നത്...", ["ആളുകളെ സ്ഥലത്ത് എത്തിച്ചിട്ട്", "പുസ്തകം വായിച്ചിട്ട്", "മരം നട്ടിട്ട്"], "യാത്രക്കാർ യാത്രയ്ക്ക് കൂലി കൊടുക്കും."),
    ("വീട്ടിൽ സഹായിക്കുന്നത്...", ["നമുക്ക് സ്നേഹം ഉള്ളതുകൊണ്ട് ചെയ്യുന്നതാ", "എപ്പോഴും പൈസ കിട്ടുന്ന കാര്യമാ", "പാടില്ലാത്ത കാര്യമാ"], "വീട്ടുകാര് പരസ്പരം സഹായിക്കും."),
    ("കടക്കാരൻ ബിസ്കറ്റിന് പൈസ വാങ്ങുന്നത് എന്തിനാ?", ["ബിസ്കറ്റിന് പൈസ കൊടുത്തതാ, അയാൾക്കും ജീവിക്കണം", "നമ്മളെ പറ്റിക്കാൻ", "ബിസ്കറ്റ് കിട്ടാനില്ലാത്തോണ്ട്"], "കടക്കാർ സാധനം വാങ്ങി വിറ്റാ പൈസ ഉണ്ടാക്കുന്നത്."),
],
"s5": [
    ("പങ്കുവെക്കൽ എന്നാൽ...", ["നമ്മുടെ കൈയിൽ ഉള്ളതിൽ കുറച്ച് മറ്റുള്ളവർക്ക് കൊടുക്കുക", "എല്ലാം നമ്മൾ തന്നെ വെക്കുക", "സാധനങ്ങൾ ഒളിപ്പിക്കുക"], "പങ്കുവെക്കുന്നത് ഒരു സഹായമാ."),
    ("ഒരു കൂട്ടുകാരന് ഉച്ചയ്ക്ക് കഴിക്കാൻ ഒന്നുമില്ല. നിനക്ക് എന്ത് ചെയ്യാം?", ["നിന്റെ ഭക്ഷണത്തിൽ നിന്ന് കുറച്ച് കൊടുക്കാം", "കളിയാക്കാം", "നിന്റെ ഭക്ഷണം ഒളിപ്പിക്കാം"], "ഭക്ഷണം പങ്കുവെക്കുന്നത് നല്ല കാര്യമാ."),
    ("പൈസ നല്ല രീതിയിൽ ഉപയോഗിക്കുന്നത് ഏതാ?", ["ആവശ്യമുള്ളവരെ സഹായിക്കുക", "നാണയം വലിച്ചെറിയുക", "നാണയം എന്നേക്കുമായി ഒളിപ്പിക്കുക"], "നല്ല മനസ്സോടെ കൊടുക്കുന്ന പൈസ ആളുകൾക്ക് സഹായമാകും."),
    ("ഒരു ദാനപ്പെട്ടിയിൽ പൈസ ഇടുന്നത്...", ["മറ്റുള്ളവരെ സഹായിക്കാൻ", "നമുക്ക് മിഠായി വാങ്ങാൻ", "ബസ് കൂലി കൊടുക്കാൻ"], "ദാനം ആവശ്യമുള്ളവർക്ക് സഹായമാണ്."),
    ("ചെറിയ സമ്മാനം കൊടുത്താലും സഹായമാകുമോ?", ["ആകും, ചെറിയ സഹായത്തിനും വിലയുണ്ട്", "ഇല്ല, വലിയ സമ്മാനം മാത്രം", "ഉത്സവത്തിന് മാത്രം"], "ചെറിയ നന്മകളും ചേർന്ന് വലുതാകും."),
    ("ഇതിൽ ശരിയല്ലാത്തത് ഏതാ?", ["പൈസ ഇല്ലാത്ത കൂട്ടുകാരനെ കളിയാക്കുന്നത്", "പെൻസിൽ പങ്കുവെക്കുന്നത്", "പഴയ ഉടുപ്പ് കൊടുക്കുന്നത്"], "നമ്മൾ ആരെയും കളിയാക്കരുത്."),
    ("നിന്റെ ഉടുപ്പുകൾ പാകം ഇല്ലാതായി. നിനക്ക് എന്ത് ചെയ്യാം?", ["ആവശ്യമുള്ളവർക്ക് കൊടുക്കാം", "റോഡിൽ എറിയാം", "ഒളിപ്പിച്ച് വെക്കാം"], "സാധനങ്ങൾ കൈമാറുന്നത് മറ്റുള്ളവർക്ക് സഹായമാകും."),
    ("പങ്കുവെക്കുമ്പോൾ നമുക്ക് സാധാരണ എന്ത് തോന്നും?", ["സന്തോഷം", "എപ്പോഴും സങ്കടം", "ദേഷ്യം"], "നല്ലത് ചെയ്യുമ്പോൾ മനസ്സിന് സുഖം തോന്നും."),
    ("നിന്റെ കൈയിൽ 2 ലഡ്ഡു ഉണ്ട്, കൂട്ടുകാരന് ഒന്നുമില്ല. എന്ത് ചെയ്യാം?", ["ഒന്ന് അവന് കൊടുക്കാം", "രണ്ടും പെട്ടെന്ന് തിന്നാം", "ഒളിപ്പിക്കാം"], "പങ്കുവെക്കുന്നത് നല്ല കാര്യമാ."),
    ("പൈസ കൊണ്ടോ സാധനം കൊണ്ടോ ആരെയൊക്കെ സഹായിക്കാം?", ["വീട്ടുകാർ, കൂട്ടുകാർ, അയൽക്കാർ", "ആരെയും വേണ്ട", "ഓൺലൈനിലെ അപരിചിതരെ മാത്രം"], "നമുക്ക് അറിയാവുന്ന, വിശ്വാസമുള്ളവരെ സഹായിക്കാം."),
    ("പങ്കുവെക്കൽ ഭരണി എന്തിനാ?", ["മറ്റുള്ളവരെ സഹായിക്കാൻ", "കളിപ്പാട്ടം വാങ്ങാൻ മാത്രം", "നാണയം കളയാൻ"], "കൊടുക്കാൻ വേണ്ടി മാറ്റിവെച്ച പൈസയാ അതിൽ."),
    ("ശരിയോ തെറ്റോ: പണക്കാർക്ക് മാത്രമേ പങ്കുവെക്കാൻ പറ്റൂ.", ["തെറ്റ്, ആർക്കും പങ്കുവെക്കാം", "ശരി", "വലിയവർക്ക് മാത്രം"], "എല്ലാവർക്കും എന്തെങ്കിലും പങ്കുവെക്കാൻ പറ്റും."),
],
"s6": [
    ("ഒരു മിഠായിക്ക് ₹2 ആണ്. നീ ₹5 കൊടുത്താൽ ബാക്കി എത്ര കിട്ടും?", ["₹2", "₹3", "₹5"], "5 ൽ നിന്ന് 2 പോയാൽ 3 ബാക്കി."),
    ("ഒരു പഴത്തിന് ₹5 ആണ്. നീ ₹10 കൊടുത്താൽ ബാക്കി എത്ര?", ["₹5", "₹10", "₹15"], "10 ൽ നിന്ന് 5 പോയാൽ 5 ബാക്കി."),
    ("ഒരു പെൻസിലിന് ₹7 ആണ്. നീ ₹10 കൊടുത്താൽ ബാക്കി എത്ര?", ["₹3", "₹7", "₹17"], "10 ൽ നിന്ന് 7 പോയാൽ 3 ബാക്കി."),
    ("ഏതിനാ വില കുറവ്?", ["₹5", "₹8", "₹10"], "5 ആണ് ഏറ്റവും ചെറിയ സംഖ്യ."),
    ("നിന്റെ കൈയിൽ ₹20 ഉണ്ട്, ₹15 ന്റെ പുസ്തകം വാങ്ങി. ഇനി എത്ര ബാക്കി ഉണ്ട്?", ["₹5", "₹15", "₹35"], "20 ൽ നിന്ന് 15 പോയാൽ 5 ബാക്കി."),
    ("കടക്കാരൻ ₹12 എന്ന് പറഞ്ഞു. ഏത് പൈസ കൊടുത്താൽ കൃത്യമാകും?", ["₹10 ഉം ₹2 ഉം", "₹5 ഉം ₹5 ഉം", "₹2 ഉം ₹1 ഉം"], "10 ഉം 2 ഉം കൂടിയാൽ 12."),
    ("ബാക്കി കിട്ടിയ പൈസ നമ്മൾ എണ്ണി നോക്കുന്നത് എന്തിനാ?", ["ശരിയാണോ എന്ന് ഉറപ്പിക്കാൻ", "അത് കുട്ടികൾക്ക് മാത്രമുള്ള നിയമമാ", "ഒരു കാര്യവുമില്ല"], "എല്ലാവരും ബാക്കി എണ്ണി നോക്കും."),
    ("ഏതിനാ ഏറ്റവും വില കൂടുതൽ?", ["₹9", "₹15", "₹50"], "50 ആണ് ഏറ്റവും വലുത്."),
    ("രണ്ട് ബിസ്കറ്റിന് ഓരോന്നിനും ₹5 ആണ്. രണ്ടിനും കൂടി എത്രയാ?", ["₹5", "₹10", "₹25"], "5 ഉം 5 ഉം കൂടിയാൽ 10."),
    ("നിന്റെ കൈയിൽ ₹10 ഉണ്ട്. ഒരു കളിപ്പാട്ടത്തിന് ₹12 ആണ്. എന്ത് ചെയ്യാം?", ["₹2 കൂടി സമ്പാദിക്കാം", "എന്തായാലും എടുക്കാം", "ഫ്രീ ആയി ചോദിക്കാം"], "കുറച്ച് കൂടി സമ്പാദിച്ചാൽ അത് വാങ്ങാം."),
    ("വിലച്ചീട്ട് നമ്മളോട് പറയുന്നത്...", ["ഒരു സാധനത്തിന് എത്ര രൂപയാണെന്ന്", "ആരാ ഉണ്ടാക്കിയതെന്ന്", "എത്ര ഭാരം ഉണ്ടെന്ന്"], "നമ്മൾ കൊടുക്കേണ്ട തുകയാണ് വില."),
    ("₹20 ന്റെ നോട്ടുബുക്കിന് നീ ₹20 കൊടുത്തു. ബാക്കി എത്ര?", ["₹0, ബാക്കി ഇല്ല", "₹20", "₹40"], "കൃത്യമായി കൊടുത്താൽ ബാക്കി ഉണ്ടാകില്ല."),
],
"s7": [
    ("സമ്പാദ്യം സൂക്ഷിക്കാൻ സേഫായ സ്ഥലം ഏതാ?", ["വിശ്വാസമുള്ള ഒരു വലിയ ആളുടെ കൂടെ വീട്ടിൽ", "ബസ് സീറ്റിൽ", "അപരിചിതന്റെ കൈയിൽ"], "സമ്പാദ്യം വിശ്വാസമുള്ളവരുടെ കൂടെ വെക്കുക."),
    ("ഒരു അപരിചിതൻ പൈസ തരാം എന്ന് പറഞ്ഞ് കൂടെ വരാൻ വിളിക്കുന്നു. നീ എന്ത് ചെയ്യും?", ["വേണ്ട എന്ന് പറഞ്ഞ് വലിയ ഒരാളോട് പറയും", "കൂടെ പോകും", "പൈസ വാങ്ങും"], "അപരിചിതരുടെ കൂടെ ഒരിക്കലും പോകരുത്."),
    ("നിന്റെ രഹസ്യ പിൻ ആർക്കൊക്കെ അറിയാം?", ["നിനക്കും വേണമെങ്കിൽ അച്ഛനമ്മമാർക്കും മാത്രം", "എല്ലാ കൂട്ടുകാർക്കും", "എല്ലാവർക്കും"], "പിൻ ഒരു രഹസ്യമാ."),
    ("വഴിയിൽ നിന്ന് പൈസ കിട്ടിയാൽ നീ എന്ത് ചെയ്യും?", ["വലിയ ഒരാളോട് പറയും", "ഒളിപ്പിക്കും", "വലിച്ചെറിയും"], "ഉടമസ്ഥനെ കണ്ടുപിടിക്കാൻ വലിയവർക്ക് സഹായിക്കാൻ പറ്റും."),
    ("നിന്റെ സമ്പാദ്യം മുഴുവൻ അപരിചിതരെ കാണിക്കണോ?", ["വേണ്ട", "വേണം", "ഞായറാഴ്ച മാത്രം"], "സമ്പാദ്യം വേറെ ആരും അറിയരുത്."),
    ("ഓൺലൈനിൽ എന്തെങ്കിലും വാങ്ങുന്നതിന് മുൻപ് നീ...", ["അച്ഛനമ്മമാരോട് ചോദിക്കണം", "പെട്ടെന്ന് ക്ലിക്ക് ചെയ്യണം", "പിൻ പറഞ്ഞുകൊടുക്കണം"], "ഓൺലൈനിൽ വാങ്ങാൻ വലിയ ഒരാൾ കൂടെ വേണം."),
    ("കടക്കാരൻ ബാക്കി പൈസ തന്നാൽ നീ...", ["പോകുന്നതിന് മുൻപ് എണ്ണി നോക്കണം", "ഓടിപ്പോകണം", "വലിച്ചെറിയണം"], "ഒന്നും കുറയാതിരിക്കാൻ എണ്ണി നോക്കണം."),
    ("വലിയ തുക ആരാ സൂക്ഷിക്കേണ്ടത്?", ["നീ വിശ്വസിക്കുന്ന ഒരു വലിയ ആൾ", "ഓൺലൈനിലെ പുതിയ കൂട്ടുകാരൻ", "ആരും വേണ്ട"], "വലിയ പൈസ വിശ്വാസമുള്ള വലിയവരുടെ കൈയിലാ വേണ്ടത്."),
    ("നിനക്ക് സമ്മാനം കിട്ടി എന്ന് ഒരു മെസ്സേജ് വന്നു. ഇനി എന്ത് ചെയ്യും?", ["വലിയ ഒരാളെ കാണിക്കും", "ലിങ്കിൽ ക്ലിക്ക് ചെയ്യും", "വീട്ടുവിലാസം മറുപടി അയക്കും"], "സമ്മാനം എന്ന് പറഞ്ഞുള്ള മെസ്സേജ് മിക്കവാറും തട്ടിപ്പാ."),
    ("ഒരു കൂട്ടുകാരൻ നിന്റെ അച്ഛന്റെ ഫോൺ പിൻ ചോദിക്കുന്നു. നീ പറയും...", ["ഇല്ല, അത് രഹസ്യമാ", "ശരി", "ചിലപ്പോൾ"], "പിൻ ആരോടും പറയരുത്."),
    ("പൈസ നഷ്ടപ്പെട്ടാൽ നീ...", ["വലിയ ഒരാളോട് സത്യം പറയണം", "ഒളിപ്പിക്കണം", "കൂട്ടുകാരനെ കുറ്റം പറയണം"], "സത്യം പറഞ്ഞാൽ പ്രശ്നം പരിഹരിക്കാൻ എളുപ്പമാകും."),
    ("വീട്ടിലെ കുടുക്ക നാണയം സൂക്ഷിക്കാൻ നല്ല സ്ഥലമാണോ?", ["അതെ", "അല്ല, മേൽക്കൂരയാ നല്ലത്", "അല്ല, അപരിചിതർക്ക് കൊടുക്കണം"], "അത് സേഫാണ്, എണ്ണാനും എളുപ്പം."),
],
}
'''

_SOURCES['ml_bank_explore'] = r'''"""Malayalam question bank for Explorers (e1 to e7), in spoken Kerala Malayalam. Same order and option count as content.py."""

BANK = {
"e1": [
    ("നിനക്ക് ₹200 കിട്ടി, അതിന്റെ കാൽ ഭാഗം സമ്പാദിക്കാൻ വെക്കുന്നു. എത്ര സമ്പാദിക്കും?", ["₹25", "₹50", "₹100"], "200 ന്റെ കാൽ ഭാഗം 50."),
    ("പങ്കുവെക്കൽ ഭരണി എന്തിനാ?", ["മറ്റുള്ളവരെ സഹായിക്കാനോ സമ്മാനം കൊടുക്കാനോ", "കൂടുതൽ കളിപ്പാട്ടം വാങ്ങാൻ", "പൈസ ഒളിപ്പിക്കാൻ"], "പങ്കുവെക്കുമ്പോൾ ചുറ്റുമുള്ളവർക്ക് സഹായമാകും."),
    ("പൈസ ഭാഗിക്കാൻ ഏറ്റവും നല്ല സമയം എപ്പോഴാ?", ["എല്ലാം ചെലവാക്കി കഴിഞ്ഞിട്ട്", "ചെലവാക്കി തുടങ്ങുന്നതിന് മുൻപ്", "ഒരിക്കലും വേണ്ട"], "ആദ്യമേ പ്ലാൻ ചെയ്താൽ സമ്പാദ്യം സേഫാകും."),
    ("നിനക്ക് ₹100 കിട്ടി, അതിൽ 20% സമ്പാദിക്കുന്നു. എത്ര സമ്പാദിക്കും?", ["₹10", "₹20", "₹80"], "100 ന്റെ 20% എന്നാൽ 20."),
    ("പിന്നീട് വലിയ സാധനങ്ങൾ വാങ്ങാൻ സഹായിക്കുന്ന ഭരണി ഏതാ?", ["സമ്പാദ്യം", "ചെലവ്", "രണ്ടുമല്ല"], "സമ്പാദ്യം വളർന്ന് വലിയ ലക്ഷ്യങ്ങൾക്ക് ഉപകരിക്കും."),
    ("മാസം തീരുന്നതിന് മുൻപ് നിന്റെ ചെലവ് ഭരണി കാലിയായി. എന്താ നല്ലത്?", ["അടുത്ത മാസം വരെ കാത്തിരിക്കുക", "സമ്പാദ്യ ഭരണിയിൽ നിന്ന് എടുക്കുക", "കൂട്ടുകാരനോട് കടം വാങ്ങുക"], "പ്ലാനിൽ തന്നെ ഉറച്ചുനിന്ന് കാത്തിരിക്കുക."),
    ("₹200 ന്റെ പകുതി എത്രയാ?", ["₹50", "₹100", "₹150"], "200 നെ 2 കൊണ്ട് ഹരിച്ചാൽ 100."),
    ("എന്തിനാ മൂന്ന് ഭരണി ഉപയോഗിക്കുന്നത്?", ["പൈസ പല ആവശ്യങ്ങൾക്ക് വേണ്ടി പ്ലാൻ ചെയ്യാൻ", "ആളുകളെ കൺഫ്യൂഷനാക്കാൻ", "പൈസ കളയാൻ"], "ഓരോ രൂപയ്ക്കും ഓരോ പണി കൊടുക്കുകയാ ഭരണികൾ."),
    ("ഒരു കൂട്ടുകാരൻ മുഴുവൻ പൈസയും ഗെയിമിൽ കളയാൻ പറയുന്നു. സ്മാർട്ടായ തീരുമാനം ഏതാ?", ["പ്ലാനിൽ ഉറച്ചുനിൽക്കുക", "മുഴുവൻ ചെലവാക്കുക", "മുഴുവൻ പങ്കുവെക്കുക"], "പെട്ടെന്നുള്ള തോന്നലിനെക്കാൾ നല്ലത് പ്ലാൻ ആണ്."),
    ("പൈസയുടെ കാര്യത്തിൽ നല്ല ശീലം ഏതാ?", ["ആദ്യം സമ്പാദിക്കുക, പിന്നെ ചെലവാക്കുക", "ആദ്യം ചെലവാക്കുക, ബാക്കി ഉണ്ടെങ്കിൽ സമ്പാദിക്കുക", "ഒരിക്കലും സമ്പാദിക്കാതിരിക്കുക"], "ആദ്യം സമ്പാദിച്ചുവെച്ചാൽ അത് ഉറപ്പായും നടക്കും."),
    ("നീ ₹200 നെ ₹100, ₹70, ₹30 ആയി ഭാഗിച്ചു. ഏതാ ശരിയായ ആകെ തുക?", ["₹200", "₹170", "₹230"], "100 + 70 + 30 = 200."),
    ("ഓരോ മാസവും കുറച്ച് പങ്കുവെക്കുന്നത് നമ്മളെ പഠിപ്പിക്കുന്നത്...", ["മറ്റുള്ളവരെ ശ്രദ്ധിക്കാൻ", "പൈസ വെറുതെ കളയാൻ", "സമ്പാദിക്കുന്നത് നിർത്താൻ"], "കൊടുക്കുമ്പോൾ നമ്മുടെ മനസ്സിൽ ദയ വളരും."),
],
"e2": [
    ("ലാഭം എന്നാൽ എന്താ?", ["വിൽപ്പനയും ചെലവും കൂട്ടിയത്", "വിൽപ്പനയിൽ നിന്ന് ചെലവ് കുറച്ചത്", "വില മാത്രം"], "ചെലവ് കഴിഞ്ഞ് ബാക്കി കിട്ടുന്നതാ ലാഭം."),
    ("ഒരു ഗ്ലാസ് ഉണ്ടാക്കാൻ ₹6 ചെലവാകും, ₹4 ന് വിൽക്കുന്നു. എന്ത് സംഭവിക്കും?", ["₹2 ലാഭം", "ഓരോ ഗ്ലാസിനും ₹2 നഷ്ടം", "ഒരു മാറ്റവുമില്ല"], "4 കിട്ടും, പക്ഷേ 6 ചെലവായി. അപ്പോൾ 2 നഷ്ടം."),
    ("വില വല്ലാതെ കൂട്ടിയാൽ സാധാരണ എന്ത് സംഭവിക്കും?", ["കൂടുതൽ ആളുകൾ വാങ്ങും", "കുറച്ച് ആളുകളേ വാങ്ങൂ", "ഒന്നും സംഭവിക്കില്ല"], "വില കൂടിയാൽ ആളുകൾ വാങ്ങാൻ മടിക്കും."),
    ("നീ 10 ഗ്ലാസ് ₹15 ന് വിൽക്കുന്നു. എത്ര പൈസ കിട്ടും?", ["₹25", "₹150", "₹1,500"], "15 നെ 10 പ്രാവശ്യം കൂട്ടിയാൽ 150."),
    ("ഒരു ഗ്ലാസിന് ₹6 ചെലവ്, 10 എണ്ണം ഉണ്ടാക്കുന്നു. ആകെ ചെലവ് എത്ര?", ["₹16", "₹60", "₹600"], "6 നെ 10 പ്രാവശ്യം കൂട്ടിയാൽ 60."),
    ("വിൽപ്പന ₹150, ചെലവ് ₹60. ലാഭം എത്രയാ?", ["₹210", "₹90", "₹60"], "150 ൽ നിന്ന് 60 പോയാൽ 90."),
    ("നാരങ്ങയ്ക്ക് വില കൂടിയാൽ നിന്റെ ചെലവ്...", ["കൂടും", "കുറയും", "പൂജ്യമായി തന്നെ നിൽക്കും"], "സാധനങ്ങൾക്ക് വില കൂടിയാൽ ചെലവും കൂടും."),
    ("ചെലവിനെക്കാൾ കുറഞ്ഞ വിലയ്ക്ക് വിറ്റാൽ നിനക്ക്...", ["നഷ്ടം വരും", "കൂടുതൽ ലാഭം കിട്ടും", "ലാഭവും നഷ്ടവും ഇല്ലാതെ വരും"], "ഓരോ വിൽപ്പനയിലും പൈസ പോകും."),
    ("ബ്രേക്ക് ഈവൻ എന്നാൽ...", ["വിൽപ്പനയും ചെലവും ഒരുപോലെ, ലാഭവുമില്ല നഷ്ടവുമില്ല", "വലിയ ലാഭം", "സാധനം ഫ്രീ ആയി കൊടുക്കൽ"], "നിനക്ക് ലാഭവുമില്ല, നഷ്ടവുമില്ല."),
    ("മഴയുള്ള ദിവസം തണുത്ത പാനീയം ആളുകൾക്ക് അധികം വേണ്ട. എന്താ പ്രതീക്ഷിക്കേണ്ടത്?", ["വിൽപ്പന കുറയും", "വിൽപ്പന കൂടും", "വിൽപ്പന അതുപോലെ തന്നെ"], "കാലാവസ്ഥ അനുസരിച്ച് ആളുകൾക്ക് വേണ്ടത് മാറും."),
    ("ഏറ്റവും കൂടിയ വില വെക്കുന്നത് എപ്പോഴും നല്ലതാണോ?", ["അല്ല, വില കൂടിയാൽ വിൽപ്പന കുറയും", "അതെ, എപ്പോഴും", "ഞായറാഴ്ച മാത്രം"], "ശരിയായ ഒരു ബാലൻസ് കണ്ടെത്തണം."),
    ("ഒരു കട നന്നായി നടക്കാൻ എന്താ സഹായിക്കുക?", ["ന്യായമായ വിലയും നല്ല സാധനവും", "മോശം പെരുമാറ്റം", "വില ഒളിപ്പിക്കൽ"], "സന്തോഷമുള്ള കസ്റ്റമർ വീണ്ടും വരും."),
],
"e3": [
    ("നിന്റെ യുപിഐ പിൻ ചോദിക്കാൻ ആർക്കാ അവകാശമുള്ളത്?", ["ബാങ്കിന്", "ആർക്കും ഇല്ല", "ഒരു ടീച്ചർക്ക്"], "പിൻ നിന്റെ മാത്രം രഹസ്യമാ."),
    ("ഓൺലൈനിലെ ഒരു അപരിചിതൻ ഒടിപി പറഞ്ഞാൽ സമ്മാനം തരാം എന്ന് പറയുന്നു. നീ എന്ത് ചെയ്യും?", ["ഉടനെ പറഞ്ഞുകൊടുക്കും", "പറയില്ല, വിശ്വാസമുള്ള വലിയ ഒരാളോട് പറയും", "രണ്ട് സമ്മാനം ചോദിക്കും"], "ഒടിപി ആരോടും പറയരുത്."),
    ("ഒരു കടയിൽ പൈസ അടയ്ക്കാൻ ഏറ്റവും സേഫായ വഴി ഏതാ?", ["അച്ഛനമ്മമാരുടെ കൂടെ നിന്ന് അടയ്ക്കുക", "മെസ്സേജ് അയച്ച ഒരാൾക്ക് പൈസ അയക്കുക", "വേഗം ആകാൻ പിൻ പറഞ്ഞുകൊടുക്കുക"], "ശരിക്കുള്ള കടയിൽ, വിശ്വാസമുള്ള വലിയ ഒരാളുടെ കൂടെ നിന്ന് പൈസ അടയ്ക്കുക."),
    ("ഒരു ലിങ്കിൽ നിനക്ക് ഫോൺ സമ്മാനം കിട്ടി എന്ന് പറയുന്നു. എന്ത് ചെയ്യണം?", ["ക്ലിക്ക് ചെയ്ത് വാങ്ങുക", "മൈൻഡ് ചെയ്യാതെ വലിയ ഒരാളെ കാണിക്കുക", "കൂട്ടുകാർക്ക് ഫോർവേഡ് ചെയ്യുക"], "ക്ലിക്ക് ചെയ്യണ്ട. ഫ്രീ സമ്മാനം എന്ന് പറയുന്നത് മിക്കവാറും തട്ടിപ്പാ."),
    ("ബാങ്കിൽ നിന്നാണെന്ന് പറഞ്ഞ് ഒരാൾ ഒടിപി ചോദിക്കുന്നു. ശരിയായ കാര്യം ഏതാ?", ["ബാങ്ക് ഒരിക്കലും ഒടിപി ചോദിക്കില്ല", "ബാങ്ക് എപ്പോഴും ചോദിക്കും", "തിങ്കളാഴ്ച മാത്രം"], "ഒടിപി ആരോടും പറയരുത്."),
    ("യുപിഐ വഴി പൈസ വാങ്ങാൻ പിൻ അടിക്കണോ?", ["വേണ്ട, ഒരിക്കലും വേണ്ട", "വേണം, എപ്പോഴും", "വലിയ തുക ആണെങ്കിൽ മാത്രം"], "പൈസ അയക്കുമ്പോൾ മാത്രമേ പിൻ വേണ്ടൂ."),
    ("ഏത് മെസ്സേജാ തട്ടിപ്പ് പോലെ തോന്നുന്നത്?", ["അർജന്റ്! 1 മണിക്കൂറിനുള്ളിൽ നിന്റെ അക്കൗണ്ട് ക്ലോസ് ആകും, ഇവിടെ ക്ലിക്ക് ചെയ്യൂ", "അത്താഴം റെഡിയായി എന്ന് അമ്മ പറയുന്നു", "വെള്ളിയാഴ്ച ഹോംവർക്ക് കൊണ്ടുവരണം എന്ന് ടീച്ചർ പറയുന്നു"], "തട്ടിപ്പുകാർ പേടിപ്പിച്ചും തിടുക്കം കൂട്ടിയും ആണ് പറ്റിക്കുന്നത്."),
    ("ഒരു ഗെയിം ചാറ്റിലെ കൂട്ടുകാരൻ അച്ഛനമ്മമാരുടെ കാർഡ് നമ്പർ ചോദിക്കുന്നു. നീ...", ["വേണ്ട എന്ന് പറഞ്ഞ് അച്ഛനമ്മമാരോട് പറയും", "അയച്ചുകൊടുക്കും", "പകുതി അയച്ചുകൊടുക്കും"], "കാർഡ് വിവരം ഒരിക്കലും ആർക്കും കൊടുക്കരുത്."),
    ("നിന്നെ പറ്റിച്ചു എന്ന് തോന്നിയാൽ നീ...", ["ഉടനെ വിശ്വാസമുള്ള വലിയ ഒരാളോട് പറയണം", "ഒളിപ്പിച്ച് വെക്കണം", "ഒന്നും ചെയ്യാതെ ഇരിക്കണം"], "വേഗം പറഞ്ഞാൽ നഷ്ടം കുറയ്ക്കാം."),
    ("“പേയ്മെന്റ് സക്സസ്” എന്നൊരു സ്ക്രീൻഷോട്ട് കണ്ടാൽ പൈസ കിട്ടി എന്ന് ഉറപ്പിക്കാമോ?", ["ഇല്ല, ബാങ്കിന്റെയോ ആപ്പിന്റെയോ മെസ്സേജ് നോക്കണം", "ഉറപ്പിക്കാം, എപ്പോഴും", "മങ്ങിയതാണെങ്കിൽ മാത്രം"], "വ്യാജ സ്ക്രീൻഷോട്ടുകൾ ഉണ്ടാക്കാൻ എളുപ്പമാ."),
    ("ഒരു അപരിചിതൻ നിന്നിൽ നിന്ന് പൈസ “കളക്ട്” ചെയ്യാൻ റിക്വസ്റ്റ് അയക്കുന്നു. നീ...", ["റിജക്ട് ചെയ്യണം", "അപ്രൂവ് ചെയ്യാൻ പിൻ അടിക്കണം", "ഒടിപി പറയണം"], "കളക്ട് റിക്വസ്റ്റ് അപ്രൂവ് ചെയ്താൽ നിന്റെ പൈസ പോകും."),
    ("ഏതാ ശക്തമായ പാസ്‌വേഡ്?", ["അക്ഷരവും അക്കവും ചിഹ്നവും ചേർന്ന നീളമുള്ള ഒന്ന്", "1234", "നിന്റെ പിറന്നാൾ ദിവസം"], "ഊഹിക്കാൻ പറ്റാത്ത പാസ്‌വേഡാണ് കൂടുതൽ സേഫ്."),
],
"e4": [
    ("ബജറ്റ് എന്നാൽ എന്താ?", ["പൈസ എങ്ങനെ ചെലവാക്കണം എന്നതിന്റെ പ്ലാൻ", "ഒരു തരം കട", "ഒരു ബാങ്ക് കാർഡ്"], "നിന്റെ പൈസ എവിടെ പോകണം എന്ന് ബജറ്റ് പറഞ്ഞുതരും."),
    ("ബജറ്റിൽ ആദ്യം ഉൾപ്പെടുത്തേണ്ടത് എന്താ?", ["ആവശ്യങ്ങൾ", "ആഗ്രഹങ്ങൾ", "ട്രീറ്റുകൾ"], "ആവശ്യങ്ങൾ ആദ്യം."),
    ("നിന്റെ കൈയിൽ ₹400 ഉണ്ട്, സമ്പാദ്യത്തിന് ₹100 മാറ്റിവെക്കുന്നു. അത് എത്ര ശതമാനമാ?", ["10%", "25%", "50%"], "100 എന്നത് 400 ന്റെ കാൽ ഭാഗമാ."),
    ("അമിത ചെലവ് എന്നാൽ എന്താ?", ["പ്ലാൻ ചെയ്തതിനെക്കാളോ കൈയിലുള്ളതിനെക്കാളോ കൂടുതൽ ചെലവാക്കൽ", "വല്ലാതെ സമ്പാദിക്കൽ", "നാണയം എണ്ണൽ"], "ബജറ്റിന് പുറത്ത് ചെലവാക്കിയാൽ പ്രശ്നമാകും."),
    ("ചെലവ് എഴുതിവെക്കുന്നത് എന്തിനാ?", ["പൈസ എവിടെ പോകുന്നു എന്ന് കാണാൻ", "കൂടുതൽ ചെലവാക്കാൻ", "ഒളിപ്പിക്കാൻ"], "എഴുതിവെച്ചാൽ നമ്മുടെ ശീലങ്ങൾ മനസ്സിലാകും."),
    ("പുതിയ ഗെയിമിന് നിന്റെ വിനോദത്തിനുള്ള പൈസയെക്കാൾ വില ഉണ്ട്. സ്മാർട്ടായ തീരുമാനം ഏതാ?", ["കാത്തിരുന്ന് സമ്പാദിക്കുക", "സ്കൂളിന് വേണ്ട പൈസയിൽ നിന്ന് എടുക്കുക", "രഹസ്യമായി കടം വാങ്ങുക"], "ആവശ്യങ്ങൾക്കുള്ള പൈസ എടുക്കരുത്."),
    ("അടിയന്തര ഫണ്ട് എന്നാൽ...", ["പെട്ടെന്ന് വരുന്ന കാര്യങ്ങൾക്ക് വേണ്ടി മാറ്റിവെക്കുന്ന പൈസ", "കളിപ്പാട്ടത്തിനുള്ള പൈസ", "കൂട്ടുകാർക്ക് കടം കൊടുക്കാനുള്ള പൈസ"], "പെട്ടെന്ന് ചെലവ് വന്നാലും അത് നമ്മളെ രക്ഷിക്കും."),
    ("നിന്റെ മാസത്തെ പൈസ ₹300 ആണ്, പലഹാരങ്ങൾക്ക് ₹120 ചെലവാക്കി. എത്ര ബാക്കിയുണ്ട്?", ["₹120", "₹180", "₹420"], "300 ൽ നിന്ന് 120 പോയാൽ 180."),
    ("ബജറ്റിൽ നല്ല ശീലം ഏതാ?", ["വരവും ചെലവും എഴുതിവെക്കുക", "എല്ലാം ഊഹിച്ച് പറയുക", "ഒരിക്കലും നോക്കാതിരിക്കുക"], "എഴുതിവെച്ചാൽ കണക്ക് ശരിയാകും."),
    ("മാസം ₹50 സമ്പാദിക്കാൻ പ്ലാൻ ചെയ്യുന്നു. 6 മാസം കൊണ്ട് എത്രയാകും?", ["₹56", "₹300", "₹3,000"], "50 നെ 6 പ്രാവശ്യം കൂട്ടിയാൽ 300."),
    ("മാസത്തിന്റെ തുടക്കത്തിൽ തന്നെ പൈസ തീർന്നുപോയാൽ നീ എന്ത് ചെയ്യണം?", ["അടുത്ത മാസത്തെ പ്ലാൻ ശരിയാക്കണം", "മൈൻഡ് ചെയ്യാതിരിക്കണം", "കൂടുതൽ ചെലവാക്കണം"], "അതിൽ നിന്ന് പഠിച്ച് അടുത്ത തവണ നന്നാക്കുക."),
    ("ബജറ്റ് ഉണ്ടാക്കുമ്പോൾ ആദ്യത്തെ സ്റ്റെപ്പ് എന്താ?", ["നിന്റെ കൈയിൽ എത്ര പൈസ ഉണ്ടെന്ന് അറിയുക", "എന്തെങ്കിലും വാങ്ങുക", "ഒരു കൂട്ടുകാരനോട് ചോദിക്കുക"], "കൈയിൽ വരുന്ന പൈസയിൽ നിന്ന് തുടങ്ങണം."),
],
"e5": [
    ("ബാങ്ക് എന്നാൽ എന്താ?", ["പൈസ സേഫായി സൂക്ഷിക്കുകയും ലോൺ കൊടുക്കുകയും ചെയ്യുന്ന സ്ഥാപനം", "കളിപ്പാട്ടക്കട", "കളിസ്ഥലം"], "ബാങ്ക് നമ്മുടെ പൈസ സൂക്ഷിക്കും, ലോണും കൊടുക്കും."),
    ("സേവിങ്സിന് കിട്ടുന്ന പലിശ എന്നാൽ എന്താ?", ["പൈസ അവിടെ വെക്കുന്നതിന് ബാങ്ക് തരുന്ന കൂടുതൽ പൈസ", "കാർഡ് പോയാൽ കൊടുക്കേണ്ട ഫീസ്", "ഒരു തരം നാണയം"], "സമ്പാദിക്കുന്നവർക്ക് ബാങ്ക് തരുന്ന പ്രതിഫലമാണ് പലിശ."),
    ("കട്ടിലിനടിയിൽ വെക്കുന്നതിനെക്കാൾ ബാങ്ക് സേഫാകുന്നത് എന്തുകൊണ്ടാ?", ["ബാങ്ക് നല്ല സുരക്ഷയോടെ പൈസ സൂക്ഷിക്കും", "ബാങ്ക് നമ്മുടെ പൈസ ഒളിപ്പിച്ച് വെക്കും", "സേഫല്ല"], "ബാങ്കിൽ പൂട്ടും കാവലും രേഖകളും ഉണ്ട്."),
    ("ബാങ്കിൽ പൈസ കൊണ്ടുപോയി ഇടുന്നതിനെ എന്താ പറയുന്നത്?", ["നിക്ഷേപിക്കൽ (ഡെപ്പോസിറ്റ്)", "പിൻവലിക്കൽ", "കടം വാങ്ങൽ"], "ഡെപ്പോസിറ്റ് എന്നാൽ അകത്ത് ഇടുക."),
    ("അക്കൗണ്ടിൽ നിന്ന് പൈസ എടുക്കുന്നതിനെ എന്താ പറയുന്നത്?", ["പിൻവലിക്കൽ (വിത്ത്ഡ്രോ)", "നിക്ഷേപിക്കൽ", "പലിശ"], "വിത്ത്ഡ്രോ എന്നാൽ പുറത്തെടുക്കുക."),
    ("ഒരു കുട്ടിക്ക് സേവിങ്സ് അക്കൗണ്ട് തുടങ്ങാൻ ആരാ സഹായിക്കുക?", ["അച്ഛനമ്മമാരോ രക്ഷിതാവോ", "ഒരു അപരിചിതൻ", "ആരും ഇല്ല"], "കുട്ടികൾക്ക് രക്ഷിതാവിന്റെ സഹായം വേണം."),
    ("പാസ്ബുക്കോ സ്റ്റേറ്റ്മെന്റോ കാണിക്കുന്നത്...", ["വരവും ചെലവും", "കാലാവസ്ഥ", "നിന്റെ മാർക്ക്"], "പൈസയുടെ ഇടപാടുകൾ എല്ലാം അതിൽ ഉണ്ടാകും."),
    ("ബാങ്കിൽ നിന്ന് കടം വാങ്ങിയാൽ സാധാരണ തിരിച്ചടയ്ക്കേണ്ടത്...", ["പൈസയും പലിശയും", "വാങ്ങിയതിനെക്കാൾ കുറവ്", "ഒന്നും വേണ്ട"], "കടം വാങ്ങിയതിന്റെ വിലയാണ് പലിശ."),
    ("ബാലൻസ് നോക്കാൻ സേഫായ വഴി ഏതാ?", ["ബാങ്കിന്റെ ഒഫീഷ്യൽ ആപ്പോ ശാഖയോ, അച്ഛനമ്മമാരുടെ കൂടെ", "മെസ്സേജിൽ വന്ന ഒരു അറിയാത്ത ലിങ്ക്", "അപരിചിതന്റെ ഫോൺ"], "ഒഫീഷ്യൽ വഴികൾ മാത്രം ഉപയോഗിക്കുക."),
    ("എടിഎം കാർഡ് എന്തിനാ?", ["മെഷീനിൽ നിന്ന് അക്കൗണ്ടിലെ പൈസ എടുക്കാൻ", "ഗെയിം കളിക്കാൻ", "കട തുറക്കാൻ"], "കാർഡിന്റെ പിൻ രഹസ്യമായി വെക്കണം."),
    ("ഒരു ബാങ്ക് അക്കൗണ്ടിൽ കൂടുതൽ പലിശ കിട്ടുന്നത് നീ...", ["പൈസ കൂടുതൽ കാലം അവിടെ ഇടുമ്പോൾ", "ദിവസവും എടുത്ത് ചെലവാക്കുമ്പോൾ", "പിൻ ആരോടെങ്കിലും പറയുമ്പോൾ"], "സമയം കിട്ടിയാൽ സമ്പാദ്യം വളരും."),
    ("ബാങ്ക് അക്കൗണ്ടിനെ കുറിച്ച് ഒരിക്കലും ആരോടും പറയാൻ പാടില്ലാത്തത് എന്താ?", ["പിൻ, ഒടിപി, പാസ്‌വേഡ്", "ഇഷ്ടമുള്ള കളർ", "വളർത്തുമൃഗത്തിന്റെ പേര്"], "ഈ രഹസ്യങ്ങളാണ് നിന്റെ പൈസ കാക്കുന്നത്."),
],
"e6": [
    ("യുപിഐ എന്നതിന്റെ മുഴുവൻ രൂപം...", ["യൂണിഫൈഡ് പേയ്മെന്റ്സ് ഇന്റർഫേസ്", "അൾട്ര ഫോൺ ഇന്റർനെറ്റ്", "യൂണിവേഴ്സൽ പേപ്പർ ഇൻകം"], "വേഗത്തിൽ പൈസ അടയ്ക്കാൻ യുപിഐ ബാങ്കുകളെ തമ്മിൽ ബന്ധിപ്പിക്കുന്നു."),
    ("യുപിഐ പിൻ എപ്പോഴാ അടിക്കേണ്ടത്?", ["പൈസ അയക്കുമ്പോൾ മാത്രം", "പൈസ വാങ്ങുമ്പോൾ", "ഒരിക്കലും വേണ്ട"], "പൈസ വാങ്ങാൻ പിൻ ഒരിക്കലും വേണ്ട."),
    ("കടയിലെ ക്യുആർ കോഡ് എന്താ ചെയ്യുന്നത്?", ["കടയുടെ പേയ്മെന്റ് വിവരങ്ങൾ അതിലുണ്ട്", "ബിൽ പ്രിന്റ് ചെയ്യും", "വാതിൽ തുറക്കും"], "സ്കാൻ ചെയ്താൽ ആർക്കാ പൈസ പോകുന്നത് എന്ന് കാണാം."),
    ("പൈസ അടയ്ക്കുന്നതിന് മുൻപ് നീ നോക്കേണ്ടത്...", ["പേരും തുകയും", "ഫോണിന്റെ കളർ", "കാലാവസ്ഥ"], "ശരിയായ കടയും ശരിയായ തുകയും ആണോ എന്ന് ഉറപ്പാക്കുക."),
    ("അച്ഛനമ്മമാരുടെ ഫോണിൽ പൈസ അടയ്ക്കുമ്പോൾ പിൻ അടിക്കേണ്ടത് ആരാ?", ["അച്ഛനമ്മമാർ", "കടക്കാരൻ", "ഒരു കൂട്ടുകാരൻ"], "പിൻ രഹസ്യമായി തന്നെ ഇരിക്കണം."),
    ("“₹5,000 കിട്ടാൻ ₹1 അടയ്ക്കൂ” എന്ന് ഒരു മെസ്സേജ് പറയുന്നു. ഇത്...", ["ഒരു തട്ടിപ്പാ", "സേഫാ", "ഒരു ബാങ്ക് നിയമമാ"], "ശരിക്കുള്ള സമ്മാനത്തിന് ആരും ആദ്യം പൈസ ചോദിക്കില്ല."),
    ("പേയ്മെന്റ് സക്സസ് ആയി എന്നതിന് തെളിവ് എന്താ?", ["ആപ്പിൽ വരുന്ന സക്സസ് മെസ്സേജ്", "ഒരു കൂട്ടുകാരൻ പറയുന്നത്", "ഒരു സ്ക്രീൻഷോട്ട് മാത്രം"], "ആപ്പ് തുറന്ന് നോക്കണം."),
    ("പൈസ അടയ്ക്കാൻ പബ്ലിക് വൈഫൈ ഉപയോഗിക്കുന്നത് സേഫാണോ?", ["അപകടമാ, മൊബൈൽ ഡാറ്റയോ വിശ്വാസമുള്ള വൈഫൈയോ ഉപയോഗിക്കണം", "എപ്പോഴും സേഫാ", "രാത്രി മാത്രം"], "പബ്ലിക് നെറ്റ്‌വർക്ക് ആരെങ്കിലും ചോർത്തിയെന്ന് വരാം."),
    ("തെറ്റായ യുപിഐ ഐഡി ടൈപ്പ് ചെയ്താൽ എന്ത് സംഭവിക്കാം?", ["പൈസ വേറെ ആൾക്ക് പോകും", "ഒന്നും സംഭവിക്കില്ല", "പൈസ ഇരട്ടിയാകും"], "ഐഡി ശ്രദ്ധിച്ച് നോക്കി അടിക്കണം."),
    ("ഫോൺ ലോക്ക് ചെയ്ത് വെക്കുന്നത് എന്തിനാ?", ["വേറെ ആർക്കും നിന്റെ ആപ്പുകൾ ഉപയോഗിക്കാൻ പറ്റാതിരിക്കാൻ", "ബാറ്ററി ലാഭിക്കാൻ", "ഗെയിം ഒളിപ്പിക്കാൻ"], "ലോക്ക് ഉണ്ടെങ്കിൽ പേയ്മെന്റ് ആപ്പുകൾ സേഫാണ്."),
    ("കുട്ടികൾ യുപിഐ ഒറ്റയ്ക്ക് ഉപയോഗിക്കണോ?", ["അച്ഛനമ്മമാരുടെ സഹായത്തോടെ ഉപയോഗിക്കണം", "വേണം, ഒറ്റയ്ക്ക്, എപ്പോഴും", "പിൻ കൂട്ടുകാരോട് പറയണം"], "വിശ്വാസമുള്ള ഒരു വലിയ ആൾ കൂടെ ഉണ്ടാകണം."),
    ("തെറ്റി പൈസ അടച്ചുപോയാൽ നീ എന്ത് ചെയ്യണം?", ["അച്ഛനമ്മമാരോട് പറഞ്ഞ് ബാങ്കിനെയോ ആപ്പിന്റെ സഹായ കേന്ദ്രത്തെയോ വിളിക്കണം", "വീണ്ടും അടയ്ക്കണം", "മൈൻഡ് ചെയ്യാതിരിക്കണം"], "ഒഫീഷ്യൽ വഴിയിലൂടെ വേഗം അറിയിക്കണം."),
],
"e7": [
    ("നല്ല ലക്ഷ്യം എന്ത്, എത്ര, എപ്പോഴത്തേക്ക് എന്ന് പറയണം. ഏതാ ഏറ്റവും നല്ലത്?", ["10 ആഴ്ചയ്ക്കുള്ളിൽ ₹500 വിലയുള്ള ഒരു ഫുട്ബോൾ വേണം", "എപ്പോഴെങ്കിലും എന്തെങ്കിലും വേണം", "എനിക്ക് പൈസ വേണം"], "വ്യക്തമായ ലക്ഷ്യത്തിൽ എത്താൻ എളുപ്പമാ."),
    ("ഒരു ലക്ഷ്യത്തിന് ₹600 വേണം. മാസം ₹100 വീതം സമ്പാദിക്കുന്നു. എത്ര മാസം വേണം?", ["3", "6", "60"], "600 നെ 100 കൊണ്ട് ഹരിച്ചാൽ 6."),
    ("ആഴ്ചയിൽ ₹50 വീതം സമ്പാദിക്കുന്നു. 4 ആഴ്ച കൊണ്ട് എത്ര ആകും?", ["₹54", "₹200", "₹500"], "50 നെ 4 പ്രാവശ്യം കൂട്ടിയാൽ 200."),
    ("വലിയ ലക്ഷ്യത്തെ ചെറിയ സ്റ്റെപ്പുകളായി ഭാഗിച്ചാൽ അത്...", ["എളുപ്പമാകും", "ബുദ്ധിമുട്ടാകും", "നടക്കില്ല"], "ചെറിയ സ്റ്റെപ്പുകൾ ചെയ്യാൻ എളുപ്പം തോന്നും."),
    ("ദീർഘകാല ലക്ഷ്യത്തിന് ഏതാ നല്ലത്?", ["കുറച്ച് കുറച്ചായി സ്ഥിരമായി സമ്പാദിക്കുക", "വെറുതെ കാത്തിരിക്കുക", "ചെലവാക്കിയിട്ട് കടം വാങ്ങുക"], "സ്ഥിരമായി സമ്പാദിച്ചാൽ ഫലം കിട്ടും."),
    ("നിന്റെ കൈയിൽ ₹200 ഉണ്ട്, ലക്ഷ്യം ₹500 ആണ്. ഇനി എത്ര വേണം?", ["₹200", "₹300", "₹700"], "500 ൽ നിന്ന് 200 പോയാൽ 300."),
    ("ഒരു കൂട്ടുകാരൻ ദിവസവും മധുരം വാങ്ങുന്നു. നിന്നെ ശരിയായ വഴിയിൽ നിർത്തുന്നത് എന്താ?", ["നിന്റെ ലക്ഷ്യം ഓർക്കുക", "അവനെ കണ്ട് അതുപോലെ ചെയ്യുക", "സമ്പാദിക്കുന്നത് നിർത്തുക"], "ലക്ഷ്യം ഉണ്ടെങ്കിൽ നമുക്ക് ഒരു കാരണം ഉണ്ടാകും."),
    ("സമ്പാദ്യം ചാർട്ടിൽ രേഖപ്പെടുത്തുന്നത് സഹായിക്കുന്നത് എന്തുകൊണ്ടാ?", ["എത്രത്തോളം എത്തി എന്ന് കാണാം", "അതിന് പൈസ ചെലവാകും", "അത് വേഗത കുറയ്ക്കും"], "പുരോഗതി കാണുമ്പോൾ മുന്നോട്ട് പോകാൻ തോന്നും."),
    ("ഒരു സ്വപ്നം നടക്കാൻ ഒരുപാട് പൈസ വേണം. നിനക്ക് എന്ത് ചെയ്യാം?", ["പ്ലാൻ ചെയ്ത്, സമ്പാദിച്ച്, ക്ഷമയോടെ കാത്തിരിക്കാം", "ഉടനെ ഉപേക്ഷിക്കാം", "ചോദിക്കാതെ എടുക്കാം"], "ക്ഷമയും പ്ലാനും ഉണ്ടെങ്കിൽ സ്വപ്നം നടക്കും."),
    ("ഒരു കളിപ്പാട്ടം വാങ്ങാനുള്ള ലക്ഷ്യം ഒരു...", ["പ്ലാൻ ചെയ്ത ആഗ്രഹമാ", "ആവശ്യമാ", "മരുന്നാ"], "പ്ലാൻ ചെയ്താൽ ആഗ്രഹങ്ങളും നല്ലതാ."),
    ("നീ ലക്ഷ്യത്തിൽ എത്തി, നേരത്തെ തന്നെ. ഇനി എന്ത് ചെയ്യാം?", ["ആഘോഷിച്ചിട്ട് പുതിയ ലക്ഷ്യം വെക്കാം", "പൈസ ഒളിപ്പിക്കാം", "ഇനി ഒരിക്കലും സമ്പാദിക്കാതിരിക്കാം"], "ആ ശീലം തുടരണം."),
    ("ലക്ഷ്യത്തിൽ എത്താൻ കൂടുതൽ സമയം എടുക്കാൻ കാരണം എന്താ?", ["സമ്പാദിച്ച പൈസ ചെലവാക്കുന്നത്", "കൂടുതൽ സമ്പാദിക്കുന്നത്", "നാണയം എണ്ണുന്നത്"], "ചെലവാക്കിയാൽ വേഗം കുറയും."),
],
}
'''

_SOURCES['ml_bank_pioneer'] = r'''"""Malayalam question bank for Pioneers (p1 to p8), in spoken Kerala Malayalam. Same order and option count as content.py."""

BANK = {
"p1": [
    ("₹1,000 വർഷം 10% വീതം കൂട്ടുപലിശയിൽ വളരുന്നു. 2 വർഷം കഴിയുമ്പോൾ എത്രയാകും?", ["₹1,200", "₹1,210", "₹1,100"], "ആദ്യ വർഷം 1,100 ആകും. പിന്നെ 1,100 ന്റെ 10% ആയ 110 കൂടി ചേരും."),
    ("കൂട്ടുപലിശ നന്നായി കിട്ടാൻ ഏറ്റവും സഹായിക്കുന്നത് എന്താ?", ["നേരത്തെ തുടങ്ങി, നിക്ഷേപിച്ചത് അങ്ങനെ തന്നെ വിടുക", "വലുതാകുന്നത് വരെ കാത്തിരിക്കുക", "പലിശ അപ്പപ്പോൾ ചെലവാക്കുക"], "സമയം കൂടുതൽ കിട്ടിയാൽ വളർച്ചയുടെ മേൽ വീണ്ടും വളർച്ച വരും."),
    ("മുൻപത്തെ പലിശയ്ക്ക് കൂടി കിട്ടുന്ന പലിശയെ എന്താ പറയുന്നത്?", ["സാധാരണ പലിശ", "കൂട്ടുപലിശ", "പോക്കറ്റ് മണി"], "അതാണ് കൂട്ടുപലിശ."),
    ("₹100 വർഷം 10% വീതം കൂട്ടുപലിശയിൽ 3 വർഷം വളരുന്നു. ഏകദേശം എത്രയാകും?", ["₹130", "₹133", "₹300"], "100 നെ 1.1 കൊണ്ട് മൂന്ന് തവണ ഗുണിച്ചാൽ 133.1 കിട്ടും."),
    ("പൈസ ഇരട്ടിയാകാൻ ഏകദേശം 72 നെ വർഷത്തെ നിരക്ക് കൊണ്ട് ഹരിച്ചത്ര വർഷം വേണം എന്നാണ് 72 ന്റെ നിയമം. 8% ആണെങ്കിൽ എത്ര വർഷം?", ["ഏകദേശം 9", "ഏകദേശം 18", "ഏകദേശം 72"], "72 നെ 8 കൊണ്ട് ഹരിച്ചാൽ 9."),
    ("ഒരേ നിരക്കിൽ ഏതാ കൂടുതൽ വളരുക: ₹1,000 10 വർഷത്തേക്കോ 20 വർഷത്തേക്കോ?", ["20 വർഷം", "10 വർഷം", "രണ്ടും ഒരുപോലെ"], "സമയമാണ് ഏറ്റവും വലിയ കാര്യം."),
    ("സാധാരണ പലിശ കിട്ടുന്നത്...", ["ആദ്യത്തെ തുകയ്ക്ക് മാത്രം", "പലിശയ്ക്ക് മാത്രം", "ഒന്നിനും കിട്ടില്ല"], "കൂട്ടുപലിശയിൽ മാത്രമേ മുൻപത്തെ പലിശയ്ക്കും പലിശ കിട്ടൂ."),
    ("“നേരത്തെ തുടങ്ങണം” എന്ന് ആളുകൾ പറയുന്നത് എന്തുകൊണ്ടാ?", ["പൈസയ്ക്ക് വളരാൻ കൂടുതൽ സമയം കിട്ടും", "ബാങ്ക് നേരത്തെ തുറക്കും", "അതൊരു നിയമമാണ്"], "നേരത്തെ ഇട്ട പൈസയ്ക്ക് കൂടുതൽ കാലം കൂട്ടുപലിശ കിട്ടും."),
    ("വളർച്ച 0% ആണെങ്കിൽ കൂട്ടുപലിശ...", ["ഒന്നും ചെയ്യില്ല", "പൈസ ഇരട്ടിയാക്കും", "പൈസ മൂന്നിരട്ടിയാക്കും"], "വളർച്ച ഇല്ലെങ്കിൽ കൂട്ടാൻ ഒന്നും ഇല്ല."),
    ("മാസം മാസം സമ്പാദിക്കുന്നതും കൂട്ടുപലിശയും ചേരുമ്പോൾ ഗുണം വരുന്നത് എന്തുകൊണ്ടാ?", ["ഓരോ നിക്ഷേപവും വളർന്നു തുടങ്ങുന്നതുകൊണ്ട്", "ബാങ്ക് മറന്നുപോകുന്നതുകൊണ്ട്", "റിസ്ക് ഒന്നും ഇല്ലാതാകുന്നതുകൊണ്ട്"], "ചെറിയ തുകകൾ സ്ഥിരമായി ഇട്ടാൽ കാലം കൊണ്ട് വലുതാകും."),
    ("ഒരു ഗെയിമിൽ കാണിക്കുന്ന വളർച്ചാ നിരക്ക്...", ["ഒരു ഉദാഹരണം മാത്രം, ഉറപ്പ് ഒന്നുമില്ല", "ഉറപ്പുള്ളതാ", "നിയമവിരുദ്ധമാ"], "ശരിക്കുള്ള ആദായം മാറിക്കൊണ്ടിരിക്കും."),
    ("എല്ലാ വർഷവും പലിശ എടുത്ത് മാറ്റിയാൽ എന്ത് സംഭവിക്കും?", ["കൂട്ടുപലിശ കുറയും", "കൂട്ടുപലിശ കൂടും", "നികുതി ഇല്ലാതാകും"], "പലിശ അതിൽ തന്നെ ഇട്ടാലേ അതും വളരൂ."),
],
"p2": [
    ("നിക്ഷേപിക്കുന്നവർ പൈസ പല ഇടത്തായി ഭാഗിച്ച് ഇടുന്നത് എന്തിനാ?", ["ഒരു വലിയ നഷ്ടം വരാനുള്ള സാധ്യത കുറയ്ക്കാൻ", "കൂടുതൽ നികുതി അടയ്ക്കാൻ", "അത് ഒരു നിയമമായതുകൊണ്ട്"], "ഒന്ന് വീണാലും ബാക്കിയുള്ളവ പിടിച്ചുനിൽക്കും."),
    ("ഓഹരി (ഷെയർ) എന്നാൽ...", ["ഒരു കൂട്ടുകാരന് കൊടുക്കുന്ന ലോൺ", "ഒരു കമ്പനിയുടെ ചെറിയ ഒരു ഭാഗത്തിന്റെ ഉടമസ്ഥത", "ഒരു തരം നാണയം"], "ഷെയർ ഉള്ളവർ കമ്പനിയുടെ ഒരു ചെറിയ ഭാഗത്തിന്റെ ഉടമകളാ."),
    ("കൂടുതൽ ആദായം കിട്ടാൻ സാധ്യതയുള്ളതിന്റെ കൂടെ സാധാരണ ഉണ്ടാകുന്നത്...", ["കൂടുതൽ റിസ്ക്", "റിസ്ക് ഒട്ടും ഇല്ലായ്മ", "ഉറപ്പുള്ള ലാഭം"], "വലിയ നേട്ടത്തിന് സാധ്യതയുള്ളിടത്ത് വലിയ നഷ്ടത്തിനും സാധ്യതയുണ്ട്. ഒന്നും ഉറപ്പില്ല."),
    ("എൻഎസ്ഇയും ബിഎസ്ഇയും...", ["ഇന്ത്യയിലെ ഓഹരി വിപണികൾ", "ബാങ്കുകൾ", "സ്കൂളുകൾ"], "ഷെയറുകൾ വാങ്ങുകയും വിൽക്കുകയും ചെയ്യുന്ന സ്ഥലങ്ങളാ അവ."),
    ("ഡൈവേഴ്സിഫിക്കേഷൻ എന്നാൽ എന്താ?", ["പൈസ മുഴുവൻ ഒരിടത്ത് ഇടാതിരിക്കൽ", "എല്ലാം ചെലവാക്കൽ", "ഒരു ഷെയർ മാത്രം വാങ്ങൽ"], "പല ഇടത്ത് ഇട്ടാൽ റിസ്ക് കുറയും."),
    ("സെൻസെക്സും നിഫ്റ്റിയും...", ["വലിയ കുറേ കമ്പനികളെ നോക്കി വിപണിയുടെ പോക്ക് കാണിക്കുന്ന സൂചികകൾ", "ബാങ്കുകളുടെ പേരുകൾ", "നാണയങ്ങൾ"], "വിപണി മൊത്തത്തിൽ എങ്ങോട്ടാ പോകുന്നത് എന്ന് അവ കാണിക്കും."),
    ("ഷെയറിന്റെ വില മാറിക്കൊണ്ടിരിക്കുന്നത്...", ["വാങ്ങുന്നവരും വിൽക്കുന്നവരും മനസ്സ് മാറ്റുന്നതുകൊണ്ട്", "ഒരു ടീച്ചർ തീരുമാനിക്കുന്നതുകൊണ്ട്", "അത് ഒരിക്കലും മാറില്ല"], "ആവശ്യവും വാർത്തകളും വിലയെ മാറ്റും."),
    ("അടുത്ത മാസത്തെ ഫീസ് പോലെ പെട്ടെന്ന് വേണ്ട പൈസ...", ["റിസ്കുള്ള നിക്ഷേപത്തിൽ ഇടരുത്", "ഷെയറിൽ ഇടണം", "അപരിചിതർക്ക് കടം കൊടുക്കണം"], "അടുത്ത് തന്നെ വേണ്ട പൈസ സേഫായി വെക്കണം."),
    ("ഇന്ത്യയിൽ ഓഹരി വിപണിയെ നിയന്ത്രിക്കുന്നത് ആരാ?", ["സെബി", "സ്കൂൾ ബോർഡ്", "തപാൽ വകുപ്പ്"], "സെബി നിക്ഷേപകരെ സംരക്ഷിക്കുന്നു."),
    ("ഡിവിഡന്റ് എന്നാൽ...", ["കമ്പനിയുടെ ലാഭത്തിൽ നിന്ന് ഒരു ഭാഗം ഷെയർ ഉടമകൾക്ക് കൊടുക്കുന്നത്", "ഒരു പിഴ", "ഒരു തരം ലോൺ"], "ചില കമ്പനികൾ ലാഭം ഷെയർ ഉടമകളുമായി പങ്കുവെക്കും."),
    ("ഇന്ത്യയിൽ ഒരു കുട്ടിയുടെ നിക്ഷേപ അക്കൗണ്ട് ആരാ നോക്കി നടത്തുന്നത്?", ["അച്ഛനമ്മമാരോ രക്ഷിതാവോ", "കുട്ടി ഒറ്റയ്ക്ക്", "ഒരു അപരിചിതൻ"], "പ്രായപൂർത്തി ആകാത്തവർക്ക് വേണ്ടി രക്ഷിതാക്കളാ അക്കൗണ്ട് നടത്തുന്നത്."),
    ("ഏത് പറച്ചിലാ ശരി?", ["മുൻപത്തെ പ്രകടനം നോക്കി ഭാവിയിലെ ഫലം ഉറപ്പിക്കാൻ പറ്റില്ല", "ഷെയർ ഒരിക്കലും വീഴില്ല", "എല്ലാവരും പെട്ടെന്ന് പണക്കാരാകും"], "വില കൂടാം, കുറയുകയും ചെയ്യാം."),
],
"p3": [
    ("വില വർഷം 6% കൂടുന്നു. ₹100 ന്റെ ഒരു പലഹാരത്തിന് ഒരു വർഷം കഴിയുമ്പോൾ എത്ര ആകും?", ["₹94", "₹106", "₹160"], "100 ന്റെ 6% എന്നാൽ 6. അപ്പോൾ വില 106."),
    ("വിലക്കയറ്റം (ഇൻഫ്ലേഷൻ) എന്നാൽ എന്താ?", ["കാലം കഴിയുംതോറും വില കൂടുന്നത്", "പൈസയുടെ ഭാരം കൂടുന്നത്", "ബാങ്കുകൾ പൂട്ടിപ്പോകുന്നത്"], "സാധനങ്ങളുടെ വില പൊതുവെ കൂടുന്നതാണ് വിലക്കയറ്റം."),
    ("10 വർഷം അലമാരയിൽ വെച്ച പൈസ മിക്കവാറും...", ["ഇന്നത്തെക്കാൾ കൂടുതൽ വാങ്ങാൻ പറ്റും", "ഇന്നത്തെക്കാൾ കുറച്ചേ വാങ്ങാൻ പറ്റൂ", "ഇന്നത്തെ അതേ അളവ് വാങ്ങാം"], "വില കൂടുന്നതുകൊണ്ട് അതേ പൈസ കൊണ്ട് കുറച്ചേ കിട്ടൂ."),
    ("ബാങ്ക് 4% തരുന്നു, വില 6% കൂടുന്നു. നിന്റെ പൈസയുടെ വാങ്ങൽ ശേഷി...", ["കുറയും", "കൂടും", "അതുപോലെ തന്നെ നിൽക്കും"], "വില നിന്റെ സമ്പാദ്യത്തെക്കാൾ വേഗത്തിൽ കൂടി."),
    ("10% വാർഷിക വിലക്കയറ്റം ഉണ്ടെങ്കിൽ ₹100 ന്റെ പലഹാരത്തിന് 2 വർഷം കഴിയുമ്പോൾ എത്ര ആകും?", ["₹110", "₹120", "₹121"], "100 നെ 1.1 കൊണ്ട് രണ്ട് തവണ ഗുണിച്ചാൽ 121."),
    ("പണ്ട് സാധനങ്ങൾക്ക് വില കുറവായിരുന്നു എന്ന് മുത്തശ്ശനും മുത്തശ്ശിയും പറയുന്നത് എന്തുകൊണ്ടാ?", ["വിലക്കയറ്റം കാരണം വില കൂടിയതുകൊണ്ട്", "കടക്കാർ കള്ളം പറഞ്ഞതുകൊണ്ട്", "നോട്ടിന്റെ വലിപ്പം കുറഞ്ഞതുകൊണ്ട്"], "വർഷങ്ങൾ കൊണ്ട് വില കൂടിക്കൂടി വന്നു."),
    ("വിലക്കയറ്റത്തെ തോൽപ്പിക്കണമെങ്കിൽ സമ്പാദ്യം വളരേണ്ടത്...", ["വില കൂടുന്നതിനെക്കാൾ വേഗത്തിൽ", "വില കൂടുന്നതിനെക്കാൾ പതുക്കെ", "വളരണ്ട ആവശ്യമേ ഇല്ല"], "വളർച്ച വിലക്കയറ്റത്തെ മറികടക്കണം."),
    ("കുറേ വർഷം കൊണ്ട് സാധാരണ കൂടുതൽ വില കൂടുന്നത് ഏതിനാ?", ["സിനിമാ ടിക്കറ്റിനും സ്കൂൾ ഫീസിനും", "ഒന്നിനും ഇല്ല", "വായുവിന്"], "മിക്ക വിലയും പതുക്കെ പതുക്കെ മുകളിലേക്ക് പോകും."),
    ("പോക്കറ്റ് മണി അതുപോലെ തന്നെ നിൽക്കുകയും വില കൂടുകയും ചെയ്താൽ നിനക്ക് വാങ്ങാൻ പറ്റുന്നത്...", ["കുറച്ച്", "കൂടുതൽ", "അതേ അളവ്"], "വാങ്ങൽ ശേഷി കുറയും."),
    ("വിലക്കയറ്റം കുറവാണ് എന്ന് പറഞ്ഞാൽ വില കൂടുന്നത്...", ["കുറച്ചുകൂടി പതുക്കെയാ", "കുറച്ചുകൂടി വേഗത്തിലാ", "ഇനി ഒരിക്കലും കൂടില്ല"], "വില കൂടുന്നുണ്ട്, വേഗം കുറവാണെന്ന് മാത്രം."),
    ("ഒരുപാട് കാലത്തേക്ക് വിലക്കയറ്റത്തിൽ നിന്ന് പൈസയെ രക്ഷിക്കാൻ ഏതാ സഹായിക്കുക?", ["വളരാൻ വേണ്ടി ബുദ്ധിയോടെ നിക്ഷേപിക്കുക", "പൈസ ഒളിപ്പിച്ച് വെക്കുക", "ഇപ്പോൾ തന്നെ എല്ലാം ചെലവാക്കുക"], "പിടിച്ചുനിൽക്കാൻ പൈസ വളരണം. ഒന്നും ഉറപ്പില്ല."),
    ("വിലയിടിവ് (ഡിഫ്ലേഷൻ) എന്നാൽ...", ["വില കുറയുന്നത്", "വില കൂടുന്നത്", "പൈസ ഇല്ലാത്ത അവസ്ഥ"], "വിലക്കയറ്റത്തിന്റെ നേരെ എതിരാ അത്."),
],
"p4": [
    ("സ്ഥിര നിക്ഷേപം (എഫ്ഡി) എന്നാൽ എന്താ?", ["കുറച്ച് കാലത്തേക്ക് ഉറപ്പിച്ച പലിശയിൽ ബാങ്കിൽ ഇടുന്ന പൈസ", "ഒരു കമ്പനിയിലെ ഷെയർ", "ഒരു കൂട്ടുകാരൻ തരുന്ന ലോൺ"], "എഫ്ഡിയിൽ പലിശ എത്രയാണെന്ന് മുൻകൂട്ടി അറിയാം."),
    ("മ്യൂച്വൽ ഫണ്ട് എന്നാൽ...", ["പലരുടെയും പൈസ ഒരുമിച്ച് ചേർത്ത് നിക്ഷേപിക്കുന്നത്", "ഉറപ്പായും കിട്ടുന്ന സമ്മാനം", "ബാങ്കുകൾക്ക് മാത്രമുള്ളത്"], "എല്ലാവരുടെയും പൈസ ചേർത്ത് ഫണ്ട് മാനേജർ നിക്ഷേപിക്കും."),
    ("ഏതിനാ സാധാരണ ഏറ്റവും മുൻകൂട്ടി പറയാൻ പറ്റുന്ന ആദായം?", ["ബാങ്ക് സ്ഥിര നിക്ഷേപം", "ഒരു ഷെയർ", "ഒരു ലോട്ടറി ടിക്കറ്റ്"], "എഫ്ഡിയുടെ നിരക്ക് മുൻപേ തീരുമാനിച്ചതാ."),
    ("ഏതിനാ കൂടുതൽ കയറ്റിറക്കം ഉണ്ടാകാൻ സാധ്യത?", ["ഒരു കമ്പനിയുടെ ഷെയർ", "ഒരു പാസ്ബുക്ക്", "ഒരു കുടുക്ക"], "ഷെയറിന്റെ വില മേലോട്ടും താഴോട്ടും പോകും."),
    ("സ്വർണത്തിന്റെ വില...", ["കാലം കൊണ്ട് കൂടുകയും കുറയുകയും ചെയ്യും", "ഒരിക്കലും മാറില്ല", "എപ്പോഴും കൂടിക്കൊണ്ടിരിക്കും"], "ഒരു നിക്ഷേപവും ഉറപ്പല്ല."),
    ("ആളുകൾ ഒന്നിലധികം തരം നിക്ഷേപം വെക്കുന്നത് എന്തിനാ?", ["റിസ്ക് പങ്കിട്ടു കുറയ്ക്കാൻ", "നികുതിക്കാരെ കൺഫ്യൂഷനാക്കാൻ", "എഫ്ഡി നിയമവിരുദ്ധമായതുകൊണ്ട്"], "പല തരം ചേർന്നാൽ റിസ്ക് കുറയും."),
    ("മ്യൂച്വൽ ഫണ്ട് നോക്കി നടത്തുന്നത് ആരാ?", ["ഒരു പ്രൊഫഷണൽ ഫണ്ട് മാനേജർ", "ഒരു കുട്ടി", "ആരെങ്കിലും"], "എവിടെ നിക്ഷേപിക്കണം എന്ന് തീരുമാനിക്കുന്നത് ഫണ്ട് മാനേജർമാരാ."),
    ("“മുൻപത്തെ ആദായം ഭാവിയിലെ ആദായം ഉറപ്പാക്കുന്നില്ല” എന്ന് പറഞ്ഞാൽ...", ["ഭാവിയിൽ കാര്യങ്ങൾ വേറെ ആയേക്കാം", "പഴയതുപോലെ തന്നെ ആവർത്തിക്കും", "ഫണ്ടുകൾ നിയമവിരുദ്ധമാ"], "റിസ്ക് എപ്പോഴും ഓർത്തിരിക്കണം."),
    ("ബാങ്കിന് പൈസ കടം കൊടുക്കുന്നത് പോലെയുള്ളത് ഏതാ?", ["സ്ഥിര നിക്ഷേപം", "ഷെയർ", "സ്വർണ നാണയം"], "നിന്റെ പൈസ ഉപയോഗിക്കുന്നതിന് ബാങ്ക് പലിശ തരും."),
    ("ഒരു ബിസിനസിന്റെ ഒരു ഭാഗം നിനക്ക് സ്വന്തമാക്കി തരുന്നത് ഏതാ?", ["ഷെയർ", "എഫ്ഡി", "പാസ്ബുക്ക്"], "ഷെയർ ഉള്ളവർ ആ കമ്പനിയുടെ ഒരു ഭാഗത്തിന്റെ ഉടമകളാ."),
    ("ഏത് പറച്ചിലാ ശരി?", ["എല്ലാ നിക്ഷേപത്തിലും കുറച്ചൊക്കെ റിസ്ക് ഉണ്ട്", "എഫ്ഡി ഒരിക്കലും തീരില്ല", "സ്വർണം എപ്പോഴും കൂടും"], "നിക്ഷേപിക്കുന്നതിന് മുൻപ് റിസ്ക് മനസ്സിലാക്കണം."),
    ("നിക്ഷേപിക്കുന്നതിന് മുൻപ് നീ എന്ത് ചെയ്യണം?", ["പഠിക്കണം, ലക്ഷ്യം വെക്കണം, വിശ്വാസമുള്ള ഒരു വലിയ ആളോട് സംസാരിക്കണം", "ഓൺലൈനിലെ അപരിചിതരുടെ ടിപ്പ് നോക്കി ചെയ്യണം", "കടം വാങ്ങി നിക്ഷേപിക്കണം"], "ടിപ്പ് നോക്കിയോ കടം വാങ്ങിയോ ഒരിക്കലും നിക്ഷേപിക്കരുത്."),
],
"p5": [
    ("പൈസ കടം വാങ്ങിയാൽ സാധാരണ തിരിച്ചടയ്ക്കേണ്ടത്...", ["തുകയും പലിശയും", "വാങ്ങിയതിനെക്കാൾ കുറവ്", "ഒന്നും വേണ്ട"], "കടം വാങ്ങിയതിന്റെ വിലയാണ് പലിശ."),
    ("ഇഎംഐ എന്നതിന്റെ മുഴുവൻ രൂപം...", ["ഇക്വേറ്റഡ് മന്ത്‌ലി ഇൻസ്റ്റാൾമെന്റ്", "ഈസി മണി ഐഡിയ", "എക്സ്ട്രാ മണി ഇൻകം"], "ഓരോ മാസവും അടയ്ക്കേണ്ട ഒരേ തുകയാണ് അത്."),
    ("പലിശ നിരക്ക് കൂടിയാൽ നീ അടയ്ക്കേണ്ടത്...", ["ആകെ കൂടുതൽ", "ആകെ കുറവ്", "അതേ തുക"], "നിരക്ക് കൂടിയാൽ ചെലവും കൂടും."),
    ("ലോൺ കാലാവധി കൂട്ടിയാൽ സാധാരണ സംഭവിക്കുന്നത്...", ["മാസത്തെ അടവ് കുറയും, പക്ഷേ ആകെ പലിശ കൂടും", "ആകെ പലിശ കുറയും", "പലിശയേ ഉണ്ടാകില്ല"], "സമയം കൂടിയാൽ പലിശയും കൂടും."),
    ("ക്രെഡിറ്റ് കാർഡ് ബില്ലിൽ ഏറ്റവും കുറഞ്ഞ തുക മാത്രം അടച്ചാൽ...", ["പലിശ വളർന്നുകൊണ്ടിരിക്കും", "കടം പെട്ടെന്ന് തീരും", "സമ്മാനം കിട്ടും"], "അടയ്ക്കാതെ ബാക്കി നിൽക്കുന്നതിന് പലിശ വീഴും."),
    ("ഏത് ലോൺ ഉപകാരപ്പെട്ടേക്കാം?", ["പഠിക്കാൻ വേണ്ടി പ്ലാൻ ചെയ്ത് എടുക്കുന്ന ലോൺ", "പെട്ടെന്ന് തോന്നിയ ആഗ്രഹങ്ങൾ വാങ്ങാനുള്ള ലോൺ", "അപരിചിതരുടെ ആപ്പിൽ നിന്നുള്ള ലോൺ"], "ആവശ്യങ്ങൾക്ക് മാത്രം, പ്ലാനോടെ കടം വാങ്ങുക."),
    ("ക്രെഡിറ്റ് സ്കോർ കാണിക്കുന്നത്...", ["ലോൺ എത്ര വിശ്വാസത്തോടെ തിരിച്ചടയ്ക്കും എന്ന്", "നിന്റെ ഉയരം", "നിന്റെ സ്കൂൾ മാർക്ക്"], "ലോൺ തരുന്നവർ അത് നോക്കിയാണ് റിസ്ക് കണക്കാക്കുന്നത്."),
    ("ആരിൽ നിന്നാ കടം വാങ്ങേണ്ടത്?", ["വിശ്വാസമുള്ളതും നിയമപ്രകാരം പ്രവർത്തിക്കുന്നതുമായ സ്ഥാപനങ്ങളിൽ നിന്ന്", "ആരും അറിയാത്ത ലോൺ ആപ്പുകളിൽ നിന്ന്", "ഓൺലൈനിലെ അപരിചിതരിൽ നിന്ന്"], "നിയമപ്രകാരം പ്രവർത്തിക്കുന്ന സ്ഥാപനങ്ങളെ മാത്രം ആശ്രയിക്കുക."),
    ("ഒരു ലോൺ ആപ്പ് നിന്റെ ഫോണിലെ കോൺടാക്റ്റും ഫോട്ടോയും ചോദിക്കുന്നു. നീ...", ["സൂക്ഷിച്ച് അത് ഒഴിവാക്കണം", "എല്ലാം അനുവദിക്കണം", "കൂട്ടുകാർക്ക് ഷെയർ ചെയ്യണം"], "സേഫല്ലാത്ത ആപ്പുകൾ നിന്റെ വിവരങ്ങൾ ദുരുപയോഗം ചെയ്യും."),
    ("ലോൺ എടുക്കുന്നതിന് മുൻപ് നീ നോക്കേണ്ടത്...", ["പലിശ നിരക്ക്, ഫീസുകൾ, തിരിച്ചടവ് കാലാവധി", "ഫോമിന്റെ കളർ", "ആദ്യ മാസത്തെ അടവ് മാത്രം"], "ആകെ എത്ര ചെലവാകും എന്ന് അറിയണം."),
    ("കടക്കെണി ഉണ്ടാകുന്നത്...", ["പഴയ ലോൺ അടയ്ക്കാൻ വീണ്ടും കടം വാങ്ങുമ്പോൾ", "എല്ലാ മാസവും സമ്പാദിക്കുമ്പോൾ", "കൃത്യ സമയത്ത് അടയ്ക്കുമ്പോൾ"], "അതിൽ നിന്ന് ഊരിപ്പോരാൻ പ്രയാസമാ."),
    ("കാത്തിരിക്കാൻ പറ്റുമെങ്കിൽ ഏതാ നല്ല തീരുമാനം?", ["സമ്പാദിച്ചിട്ട് പിന്നീട് വാങ്ങുക", "കൂടിയ പലിശയ്ക്ക് കടം വാങ്ങുക", "ആവശ്യങ്ങൾ വേണ്ടെന്ന് വെക്കുക"], "കാത്തിരുന്നാൽ പലിശ കൊടുക്കേണ്ടി വരില്ല."),
],
"p6": [
    ("ജിഎസ്ടി എന്നാൽ...", ["സാധനങ്ങൾക്കും സേവനങ്ങൾക്കും ഉള്ള നികുതി", "ഒരു തരം ബാങ്ക്", "ഒരു സ്കൂൾ ഫീസ്"], "ജിഎസ്ടി എന്നാൽ ഗുഡ്സ് ആൻഡ് സർവീസസ് ടാക്സ്."),
    ("സർക്കാർ നികുതി പിരിക്കുന്നത് എന്തിനാ?", ["റോഡ്, സ്കൂൾ, ആശുപത്രി ഒക്കെ ഉണ്ടാക്കാൻ പൈസ കണ്ടെത്താൻ", "മധുരം വാങ്ങാൻ", "കടകൾ പൂട്ടാൻ"], "പൊതു സേവനങ്ങൾക്കുള്ള പൈസ നികുതിയിൽ നിന്നാ വരുന്നത്."),
    ("ഗ്രോസ് ശമ്പളം എന്നാൽ...", ["കുറവുകൾ വരുന്നതിന് മുൻപുള്ള ശമ്പളം", "നികുതി കഴിഞ്ഞുള്ള ശമ്പളം", "ബോണസ് മാത്രം"], "നെറ്റ് ശമ്പളമാ ശരിക്കും ബാക്കിയാകുന്നത്."),
    ("നെറ്റ് ശമ്പളം അഥവാ കൈയിൽ കിട്ടുന്ന ശമ്പളം...", ["കുറവുകൾ കഴിഞ്ഞ് കിട്ടുന്നത്", "കുറവുകൾക്ക് മുൻപുള്ള ശമ്പളം", "അടച്ച നികുതി"], "അതാണ് ശരിക്കും നിന്റെ കൈയിൽ എത്തുന്ന തുക."),
    ("പേസ്ലിപ്പ് കാണിക്കുന്നത്...", ["വരുമാനവും കുറവുകളും", "കാലാവസ്ഥ", "സ്കൂൾ മാർക്ക്"], "ശമ്പളം എങ്ങനെ കണക്കാക്കി എന്ന് അതിൽ കാണാം."),
    ("പാൻ എന്നതിന്റെ മുഴുവൻ രൂപം...", ["പെർമനന്റ് അക്കൗണ്ട് നമ്പർ", "പബ്ലിക് അസറ്റ് നോട്ട്", "പെയ്ഡ് അമൗണ്ട് നമ്പർ"], "നികുതി അടയ്ക്കുന്നവരെ തിരിച്ചറിയാനുള്ളതാ അത്."),
    ("ടിഡിഎസ് എന്നാൽ...", ["സ്രോതസ്സിൽ നിന്ന് പിടിക്കുന്ന നികുതി", "ഞായറാഴ്ച അടയ്ക്കേണ്ട നികുതി", "ആകെ ദിവസ വിൽപ്പന"], "ശമ്പളം കൈയിൽ കിട്ടുന്നതിന് മുൻപ് തന്നെ നികുതി പിടിച്ചെന്ന് വരാം."),
    ("ആദായനികുതി അടയ്ക്കേണ്ടത്...", ["ഒരു നിശ്ചിത പരിധിക്ക് മുകളിൽ വരുമാനം ഉള്ളവർ", "വഴിയിൽ നിന്ന് കിട്ടുന്ന ഓരോ നാണയത്തിനും", "സ്നേഹത്തോടെ കിട്ടുന്ന സമ്മാനത്തിന് മാത്രം"], "പരിധിയും നിരക്കും നിയമം പറയും."),
    ("ആദായനികുതി റിട്ടേൺ എന്താ ചെയ്യുന്നത്?", ["നിന്റെ വരുമാനവും നികുതിയും സർക്കാരിനെ അറിയിക്കുന്നു", "ഒരു വീട് വാങ്ങുന്നു", "ഒരു ബാങ്ക് തുടങ്ങുന്നു"], "വർഷത്തിൽ ഒരിക്കൽ കൊടുക്കുന്ന റിപ്പോർട്ടാ അത്."),
    ("ജിഎസ്ടി ഉള്ള ഒരു ബിൽ കാണിക്കുന്നത്...", ["വിലയുടെ കൂടെ ചേർത്ത നികുതി", "കടയുടെ വിലാസം മാത്രം", "വേറെ ഒന്നുമില്ല"], "ജിഎസ്ടി നീ കൊടുക്കുന്ന തുകയുടെ ഭാഗമാ."),
    ("ആദ്യ ശമ്പളം കിട്ടുമ്പോൾ ചെയ്യേണ്ട നല്ല ശീലം ഏതാ?", ["പ്ലാൻ ചെയ്യുക: ആവശ്യങ്ങൾ, സമ്പാദ്യം, പിന്നെ ആഗ്രഹങ്ങൾ", "ഒരു ദിവസം കൊണ്ട് എല്ലാം ചെലവാക്കുക", "അപരിചിതർക്ക് കടം കൊടുക്കുക"], "പൈസ പ്ലാൻ ചെയ്ത് ഉപയോഗിക്കുക."),
    ("ആരാ നികുതി അടയ്ക്കേണ്ടത്?", ["നിയമം പറയുന്നതനുസരിച്ച് വ്യക്തികളും ബിസിനസുകളും", "കുട്ടികൾ മാത്രം", "ആരും വേണ്ട"], "ഓരോരുത്തരും അവരവരുടെ കാര്യത്തിൽ നിയമം പാലിക്കണം."),
],
"p7": [
    ("പ്രോഫിറ്റ് മാർജിൻ എന്നാൽ...", ["വിൽപ്പന വിലയുടെ എത്ര ഭാഗമാണ് ലാഭം എന്ന്", "കടയുടെ വാടക", "ഒരു ഡിസ്കൗണ്ട്"], "ഓരോ വിൽപ്പനയിൽ നിന്നും നമ്മുടെ കൈയിൽ എത്ര നിൽക്കും എന്ന് അത് കാണിക്കും."),
    ("ഒരു മെഴുകുതിരി ഉണ്ടാക്കാൻ ₹40 ചെലവാകും, ₹100 ന് വിൽക്കുന്നു. ഒരു മെഴുകുതിരിയിൽ നിന്നുള്ള ലാഭം എത്ര?", ["₹40", "₹60", "₹140"], "100 ൽ നിന്ന് 40 പോയാൽ 60."),
    ("സ്ഥിര ചെലവുകൾ എന്നാൽ...", ["കടയുടെ വാടക പോലെ മാറാത്ത ചെലവുകൾ", "ഓരോ സാധനത്തിനും മാറുന്ന ചെലവുകൾ", "ഫ്രീ"], "വിൽപ്പന മാറിയാലും വാടക മാറില്ല."),
    ("മാറുന്ന ചെലവുകൾ എന്നാൽ...", ["എത്ര ഉണ്ടാക്കുന്നു എന്നതനുസരിച്ച് മാറുന്ന ചെലവുകൾ", "ഒരിക്കലും മാറാത്ത ചെലവുകൾ", "ശമ്പളം മാത്രം"], "കൂടുതൽ ഉണ്ടാക്കുമ്പോൾ സാധനങ്ങൾക്കുള്ള ചെലവും കൂടും."),
    ("സ്ഥിര ചെലവ് ₹1,000, ഒരു സാധനത്തിൽ നിന്നുള്ള ലാഭം ₹50. ബ്രേക്ക് ഈവൻ ആകാൻ എത്ര സാധനം വിൽക്കണം?", ["10", "20", "50"], "1,000 നെ 50 കൊണ്ട് ഹരിച്ചാൽ 20."),
    ("ഒരു ചെറിയ ബിസിനസ് വളരാൻ എന്താ സഹായിക്കുക?", ["സന്തോഷമുള്ള കസ്റ്റമേഴ്സും നല്ല ക്വാളിറ്റിയും", "വില ഒളിപ്പിച്ച് വെക്കൽ", "വേറൊരാളെ കോപ്പിയടിക്കൽ"], "നല്ല പേര് ഉണ്ടെങ്കിൽ വീണ്ടും വീണ്ടും ആളുകൾ വാങ്ങും."),
    ("ആദ്യം ഒരു ചെറിയ ബാച്ച് ഉണ്ടാക്കി നോക്കുന്നത് എന്തിനാ?", ["ഒരുപാട് പൈസ ഇറക്കുന്നതിന് മുൻപ് പഠിക്കാൻ", "പൈസ കളയാൻ", "കസ്റ്റമേഴ്സിനെ ഒഴിവാക്കാൻ"], "ചെറിയ പരീക്ഷണം റിസ്ക് കുറയ്ക്കും."),
    ("ലാഭം വീണ്ടും നിക്ഷേപിക്കുക എന്നാൽ...", ["ലാഭത്തിന്റെ ഒരു ഭാഗം ബിസിനസ് വലുതാക്കാൻ ഉപയോഗിക്കുക", "മുഴുവനും ട്രീറ്റിന് ചെലവാക്കുക", "ഒളിപ്പിച്ച് വെക്കുക"], "വളരണമെങ്കിൽ അതിന് വേണ്ടി പൈസ ഇറക്കണം."),
    ("മത്സരം എന്നാൽ...", ["വേറെ ആളുകളും ഇതേപോലത്തെ സാധനം വിൽക്കുന്നു", "ആരും ഒന്നും വിൽക്കുന്നില്ല", "എല്ലാം ഫ്രീ ആണ്"], "നമ്മൾ എങ്ങനെ വ്യത്യസ്തരാണ് എന്ന് ആലോചിക്കണം."),
    ("വില വല്ലാതെ കുറച്ചാൽ...", ["ലാഭം കുറയും", "എപ്പോഴും വലിയ ലാഭം കിട്ടും", "എല്ലാ ചെലവും നിൽക്കും"], "നമ്മുടെ ചെലവ് തിരിച്ചു കിട്ടുന്ന വില വേണം."),
    ("ബിസിനസ് പ്ലാനിൽ എന്തൊക്കെ ഉണ്ടാകും?", ["ലക്ഷ്യം, ചെലവ്, കസ്റ്റമേഴ്സ്, എങ്ങനെ പൈസ ഉണ്ടാക്കും എന്നത്", "ഒരു പേര് മാത്രം", "ഒരു ലോഗോ മാത്രം"], "തീരുമാനങ്ങൾ എടുക്കാൻ അത് വഴി കാണിക്കും."),
    ("ആദ്യ മാസം നിനക്ക് നഷ്ടം വന്നു. സ്മാർട്ടായ പ്രതികരണം ഏതാ?", ["പഠിച്ച്, മാറ്റം വരുത്തി, വീണ്ടും ശ്രമിക്കുക", "എന്നേക്കുമായി ഉപേക്ഷിക്കുക", "കസ്റ്റമേഴ്സിനെ കുറ്റം പറയുക"], "സംരംഭകർ തെറ്റുകളിൽ നിന്ന് പഠിക്കും."),
],
"p8": [
    ("ഫിഷിങ് എന്നാൽ...", ["വ്യാജ മെസ്സേജ് അയച്ച് ആളുകളെ പറ്റിച്ച് രഹസ്യങ്ങൾ വാങ്ങുന്നത്", "ഒരു മീൻപിടുത്ത വിനോദം", "ഒരു ബാങ്ക് ലോൺ"], "തട്ടിപ്പുകാർ ശരിക്കുള്ള സ്ഥാപനങ്ങളെ പോലെ അഭിനയിക്കും."),
    ("നീ “ഡിജിറ്റൽ അറസ്റ്റിലാണ്” എന്ന് ഒരാൾ ഫോണിൽ പറയുന്നു. നീ എന്ത് ചെയ്യണം?", ["ഫോൺ വെച്ച് വിശ്വാസമുള്ള ഒരു വലിയ ആളോട് പറയണം", "പൈസ അടയ്ക്കണം", "ആധാർ പറഞ്ഞുകൊടുക്കണം"], "ശരിക്കുള്ള പോലീസ് വീഡിയോ കോളിൽ പൈസ ചോദിക്കില്ല."),
    ("ഇന്ത്യയിലെ ദേശീയ സൈബർ ക്രൈം ഹെൽപ്പ്‌ലൈൻ നമ്പർ...", ["1930", "100000", "555"], "ഓൺലൈൻ തട്ടിപ്പ് വേഗം റിപ്പോർട്ട് ചെയ്യണം."),
    ("“ഇപ്പോൾ തന്നെ കെവൈസി അപ്ഡേറ്റ് ചെയ്യൂ, ഇല്ലെങ്കിൽ അക്കൗണ്ട് ക്ലോസ് ആകും” എന്നും ഒരു ലിങ്കും ഉള്ള മെസ്സേജ് വന്നു. നീ...", ["ബാങ്കിന്റെ ഒഫീഷ്യൽ ആപ്പ് വഴിയോ നമ്പർ വഴിയോ ബന്ധപ്പെടണം", "ലിങ്കിൽ ക്ലിക്ക് ചെയ്യണം", "ഒടിപി പറയണം"], "ഒഫീഷ്യൽ വഴികൾ മാത്രം ഉപയോഗിക്കുക."),
    ("തട്ടിപ്പിന്റെ ഏറ്റവും വലിയ സൂചന ഏതാ?", ["ഉടനെ ചെയ്യണം എന്ന് സമ്മർദ്ദം ചെലുത്തുന്നത്", "മര്യാദയുള്ള ഒരു ഹലോ", "കടയിലെ ഒരു രസീത്"], "തട്ടിപ്പുകാർ നമ്മളെ തിടുക്കം കൂട്ടിക്കും."),
    ("ടു-ഫാക്ടർ ഓതന്റിക്കേഷൻ...", ["അത് നീ തന്നെയാണെന്ന് തെളിയിക്കാൻ രണ്ടാമതൊരു സ്റ്റെപ്പ് കൂടി ചേർക്കും", "നിന്റെ പൈസ ഇരട്ടിയാക്കും", "ഫോൺ ഒളിപ്പിക്കും"], "അത് അക്കൗണ്ടിനെ കൂടുതൽ സേഫാക്കും."),
    ("പബ്ലിക് വൈഫൈ അപകടമാകുന്നത്...", ["വേറെ ആളുകൾക്ക് ഡാറ്റ ചോർത്താൻ പറ്റുന്നതുകൊണ്ട്", "അത് വളരെ സ്പീഡ് ഉള്ളതുകൊണ്ട്", "അതിന് പൈസ ചെലവാകുന്നതുകൊണ്ട്"], "പബ്ലിക് വൈഫൈയിൽ പ്രധാനപ്പെട്ട കാര്യങ്ങൾ ചെയ്യരുത്."),
    ("ഒരു കൂട്ടുകാരന്റെ അക്കൗണ്ടിൽ നിന്ന് പെട്ടെന്ന് ചാറ്റിൽ പൈസ ചോദിക്കുന്നു. നീ...", ["ആദ്യം വിളിച്ച് ഉറപ്പാക്കണം", "വേഗം പൈസ അയക്കണം", "പിൻ പറഞ്ഞുകൊടുക്കണം"], "അക്കൗണ്ട് ഹാക്ക് ചെയ്തതാകാം."),
    ("നിന്റെ വീട്ടുവിലാസവും സ്കൂളും പബ്ലിക് സോഷ്യൽ മീഡിയയിൽ ഇടണോ?", ["വേണ്ട, സ്വകാര്യ വിവരങ്ങൾ പ്രൈവറ്റായി വെക്കണം", "വേണം, എപ്പോഴും", "സമ്മാനം കിട്ടാൻ മാത്രം"], "എല്ലാം പബ്ലിക് ആക്കിയാൽ തട്ടിപ്പുകാർക്ക് എളുപ്പമാകും."),
    ("ഏത് ആപ്പ് ഉറവിടമാ ഏറ്റവും സേഫ്?", ["ഒഫീഷ്യൽ ആപ്പ് സ്റ്റോർ", "ഒരു അപരിചിതൻ അയച്ച ലിങ്ക്", "ഫോർവേഡ് ചെയ്ത ഫയൽ"], "വ്യാജ ആപ്പുകൾ ഡാറ്റ മോഷ്ടിക്കും."),
    ("90% ഡിസ്കൗണ്ടിൽ പുത്തൻ ഫോൺ തരാം എന്ന് പറയുന്ന ഒരു സൈറ്റ് മിക്കവാറും...", ["വിശ്വസിക്കാൻ പറ്റാത്തത്ര നല്ലതാ (തട്ടിപ്പ്)", "ഒരു ഗംഭീര ഡീൽ", "സർക്കാർ അംഗീകരിച്ചത്"], "വിശ്വസിക്കാൻ പറ്റാത്ത ഓഫർ ഇരയെ വീഴ്ത്താനുള്ള ചൂണ്ടയാ."),
    ("തട്ടിപ്പിൽ പെട്ടാൽ ഏറ്റവും നല്ല കാര്യം...", ["ഒരു വലിയ ആളോട് പറഞ്ഞ് ബാങ്കിനെ ബന്ധപ്പെട്ട് റിപ്പോർട്ട് ചെയ്യുക", "മിണ്ടാതിരിക്കുക", "വീണ്ടും പൈസ അടയ്ക്കുക"], "വേഗം റിപ്പോർട്ട് ചെയ്താൽ നഷ്ടം തടയാം."),
],
}
'''

_SOURCES['i18n'] = r'''"""Language layer: English (default) and Malayalam.

T("English text with {placeholders}", name=value) returns the text in the current language.
The English sentence is the key, so a missing translation simply shows English.
Lesson text (titles, stories, questions, game labels) is overlaid from the ml_* modules.
"""
import copy

import streamlit as st

import content as C
import ml_bank_explore
import ml_bank_pioneer
import ml_bank_seed
import ml_lessons
import ml_ui

MISSING = set()          # English keys that had no Malayalam yet (used by the tests)
LANGS = ("en", "ml")


def lang():
    try:
        return st.session_state.get("lang", "en")
    except Exception:
        return "en"


def T(en, **kw):
    text = en
    if lang() == "ml":
        found = ml_ui.UI.get(en)
        if found is None:
            MISSING.add(en)
        else:
            text = found
    return text.format(**kw) if kw else text


# ----------------------------------------------------------------- lessons
_BANKS = {}
_BANKS.update(ml_bank_seed.BANK)
_BANKS.update(ml_bank_explore.BANK)
_BANKS.update(ml_bank_pioneer.BANK)
try:
    from more_data import DATA as _MORE
except ImportError:
    _MORE = {}
for _lid, _items in _MORE.items():
    _BANKS[_lid] = list(_BANKS[_lid]) + [(t[4], t[5], t[6]) for t in _items]


def _merge(l, o, bank):
    m = copy.deepcopy(l)
    m["title"], m["blurb"], m["talk"] = o["title"], o["blurb"], o["talk"]
    m["badge"] = (o["badge"], l["badge"][1])
    m["story"] = [(em, txt) for (em, _), txt in zip(l["story"], o["story"])]
    act, oa, kind = m["act"], o.get("act", {}), l["act"]["type"]
    if kind == "coins":
        for r, say in zip(act["rounds"], oa["say"]):
            r["say"] = say
    elif kind == "sort":
        act["labels"] = list(oa["labels"])
        act["items"] = [(it[0], lab, it[2], why) for it, (lab, why) in zip(act["items"], oa["items"])]
    elif kind == "piggy":
        act["unit"], act["unit_pl"], act["what"] = oa["unit"], oa["unit_pl"], oa["what"]
    elif kind == "alloc":
        act["cats"] = [(k, name) for (k, _), name in zip(act["cats"], oa["cats"])]
    elif kind == "stall":
        act["product"], act["unit"] = oa["product"], oa["unit"]
        act["days"] = [(name, em, mult) for (_, em, mult), name in zip(act["days"], oa["days"])]
    elif kind == "order":
        act["steps"], act["title"] = list(oa["steps"]), oa["title"]
    m["bank"] = [(q, opts, raw[2], why) for raw, (q, opts, why) in zip(l["bank"], bank)]
    return m


_ML = {l["id"]: _merge(l, ml_lessons.META[l["id"]], _BANKS[l["id"]]) for l in C.LESSONS}


def lesson(lid):
    return _ML[lid] if lang() == "ml" else C.LESSON_BY_ID[lid]


def lessons_for(band):
    return [lesson(l["id"]) for l in C.lessons_for(band)]


def all_lessons():
    return [lesson(l["id"]) for l in C.LESSONS]


def question(lid, idx):
    return lesson(lid)["bank"][idx]


def bands():
    out = []
    for b in C.BANDS:
        if lang() == "ml":
            o = ml_ui.BANDS[b["id"]]
            out.append(dict(id=b["id"], name=o["name"], ages=o["ages"], note=o["note"], ages_short=o["short"]))
        else:
            out.append(dict(id=b["id"], name=b["name"], ages=b["ages"], note=b["note"], ages_short=b["ages"].replace("Ages ", "")))
    return out


def band(bid):
    return next(b for b in bands() if b["id"] == bid)


def validate():
    """Raise if the Malayalam text does not line up with the English content."""
    for l in C.LESSONS:
        ml = _ML[l["id"]]
        assert len(ml["bank"]) == len(l["bank"]) >= 12, l["id"]
        for en, m in zip(l["bank"], ml["bank"]):
            assert len(en[1]) == len(m[1]), (l["id"], en[0])
            assert m[0].strip() and all(o.strip() for o in m[1]) and m[3].strip(), (l["id"], en[0])
        o = ml_lessons.META[l["id"]]
        assert len(o["story"]) == 3, l["id"]
        kind = l["act"]["type"]
        oa = o.get("act", {})
        if kind == "coins":
            assert len(oa["say"]) == len(l["act"]["rounds"]), l["id"]
        if kind == "sort":
            assert len(oa["labels"]) == len(l["act"]["labels"]) and len(oa["items"]) == len(l["act"]["items"]), l["id"]
        if kind == "alloc":
            assert len(oa["cats"]) == len(l["act"]["cats"]), l["id"]
        if kind == "stall":
            assert len(oa["days"]) == len(l["act"]["days"]), l["id"]
        if kind == "order":
            assert len(oa["steps"]) == len(l["act"]["steps"]), l["id"]
    return True
'''

_SOURCES['ui'] = r'''"""Look and feel: light, dark and auto themes, plus small HTML helpers."""
import html

import streamlit as st

LIGHT = {
    "bg": "#F3F8F6", "card": "#FFFFFF", "ink": "#16302C", "muted": "#566D68", "line": "#D9E6E2",
    "brand": "#0B7A75", "brand-ink": "#FFFFFF", "brand-soft": "#DDF1EF",
    "sun": "#F5A524", "sun-ink": "#3B2800", "sun-soft": "#FFF0D2",
    "good": "#17803F", "good-soft": "#DEF3E5", "bad": "#B8430F", "bad-soft": "#FDE6DA",
    "shadow": "0 8px 24px rgba(22,48,44,.08)", "scheme": "light",
}
DARK = {
    "bg": "#0C1A19", "card": "#15292A", "ink": "#E8F3F0", "muted": "#9DB7B1", "line": "#27403F",
    "brand": "#2FC1B8", "brand-ink": "#04211F", "brand-soft": "#17403F",
    "sun": "#F7B63F", "sun-ink": "#2A1C00", "sun-soft": "#3A2E12",
    "good": "#4BD08A", "good-soft": "#143A27", "bad": "#FF9B6B", "bad-soft": "#42241A",
    "shadow": "0 8px 24px rgba(0,0,0,.35)", "scheme": "dark",
}


def _vars(tokens):
    return ";".join(f"--{k}:{v}" for k, v in tokens.items() if k != "scheme") + f";color-scheme:{tokens['scheme']}"


def theme_css(mode):
    if mode == "dark":
        root = f":root{{{_vars(DARK)}}}"
    elif mode == "light":
        root = f":root{{{_vars(LIGHT)}}}"
    else:
        root = f":root{{{_vars(LIGHT)}}}@media (prefers-color-scheme: dark){{:root{{{_vars(DARK)}}}}}"
    return root


BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Baloo+Chettan+2:wght@600;700;800&family=Lexend:wght@400;500;600&family=Noto+Sans+Malayalam:wght@400;500;600;700&display=swap');
html,body,.stApp,[data-testid="stAppViewContainer"]{background:var(--bg)!important;color:var(--ink)}
.stApp{font-family:'Lexend','Noto Sans Malayalam',system-ui,sans-serif}
[data-testid="stHeader"]{background:transparent!important;height:0}
[data-testid="stToolbar"],[data-testid="stDecoration"],footer,#MainMenu{display:none!important}
.block-container{max-width:760px!important;padding:1rem 16px 5rem!important}
.stApp p,.stApp li,.stApp label,.stApp span,.stApp div[data-testid="stMarkdownContainer"]{color:inherit}
h1,h2,h3,.nk-title{font-family:'Baloo 2','Baloo Chettan 2','Noto Sans Malayalam','Lexend','Noto Sans Malayalam',sans-serif!important;color:var(--ink)!important;letter-spacing:0}
[data-testid="stVerticalBlock"]{gap:.7rem}

/* keep rows side by side on phones */
[class*="st-key-ns-"] [data-testid="stHorizontalBlock"]{flex-direction:row!important;flex-wrap:nowrap!important;gap:.5rem!important}
[class*="st-key-ns-"] [data-testid="stColumn"],[class*="st-key-ns-"] [data-testid="column"]{min-width:0!important}

/* buttons */
.stButton,[data-testid="stElementContainer"]:has(>.stButton),[data-testid="stButton"]{width:100%!important}
.stButton>button,[data-testid="stButton"]>button{width:100%!important;min-height:3rem;border-radius:16px;border:2px solid var(--line);background:var(--card);color:var(--ink);
  font-family:'Lexend','Noto Sans Malayalam',sans-serif;font-weight:600;box-shadow:0 3px 0 var(--line);transition:transform .08s,border-color .15s;padding:.4rem .8rem}
.stButton>button:hover{border-color:var(--brand);color:var(--brand)}
.stButton>button:active{transform:translateY(2px);box-shadow:0 1px 0 var(--line)}
.stButton>button:focus-visible{outline:3px solid var(--sun);outline-offset:2px}
.stButton>button[kind="primary"],.stButton>button[data-testid="stBaseButton-primary"]{background:var(--brand);color:var(--brand-ink);border-color:var(--brand);box-shadow:0 3px 0 rgba(0,0,0,.28)}
.stButton>button[kind="primary"]:hover,.stButton>button[data-testid="stBaseButton-primary"]:hover{filter:brightness(1.06);color:var(--brand-ink)}
.stButton>button p,.stButton>button div{color:inherit!important;margin:0;font-weight:inherit}
.stButton>button:disabled{opacity:.55;cursor:not-allowed}

/* answer states */
[class*="st-key-ok-"] .stButton>button{background:var(--good-soft);border-color:var(--good);color:var(--good);box-shadow:0 3px 0 var(--good)}
[class*="st-key-no-"] .stButton>button{background:var(--bad-soft);border-color:var(--bad);color:var(--bad);box-shadow:none;opacity:.9}
[class*="st-key-sel-"] .stButton>button{background:var(--brand-soft);border-color:var(--brand);color:var(--brand)}
[class*="st-key-tab-on"] .stButton>button{background:var(--brand);color:var(--brand-ink);border-color:var(--brand)}
[class*="st-key-tile-"] .stButton>button{min-height:4.4rem;font-size:1.05rem}
[class*="st-key-tile-"] .stButton>button p{font-size:1.05rem;line-height:1.2}
[class*="st-key-big-"] .stButton>button{min-height:3.6rem;font-size:1.1rem}

/* inputs */
[data-baseweb="input"],[data-baseweb="base-input"],.stTextInput input{background:var(--card)!important;color:var(--ink)!important;border-radius:14px!important}
[data-baseweb="input"]{border:2px solid var(--line)!important}
.stTextInput label p,.stTextInput label{color:var(--muted)!important}
.stTextInput input::placeholder{color:var(--muted)!important;opacity:.8}
.stDownloadButton>button{width:100%;border-radius:16px;border:2px solid var(--line);background:var(--card);color:var(--ink);min-height:3rem;font-weight:600}
.stDownloadButton>button p{color:inherit!important}
[data-testid="stAlert"]{border-radius:14px}

/* cards */
[class*="st-key-card-"]{background:var(--card);border:2px solid var(--line);border-radius:22px;padding:14px 16px;box-shadow:var(--shadow)}
.nk-hero{background:linear-gradient(135deg,var(--brand),#065a57);color:#fff;border-radius:26px;padding:18px 18px 16px;box-shadow:var(--shadow);position:relative;overflow:hidden}
.nk-hero *{color:#fff!important}
.nk-hero .nk-title{font-size:1.65rem;font-weight:800;line-height:1.15;margin:0 0 4px}
.nk-hero small{opacity:.9}
.nk-mascot{position:absolute;right:12px;top:8px;font-size:3.1rem;filter:drop-shadow(0 4px 0 rgba(0,0,0,.18))}
.nk-card{background:var(--card);border:2px solid var(--line);border-radius:22px;padding:14px 16px;box-shadow:var(--shadow)}
.nk-title{font-weight:800;font-size:1.25rem;margin:0}
.nk-sub{color:var(--muted)!important;font-size:.92rem;margin:2px 0 0}
.nk-row{display:flex;align-items:center;gap:12px}
.nk-art{width:54px;height:54px;border-radius:16px;background:var(--brand-soft);display:grid;place-items:center;font-size:1.9rem;flex:none}
.nk-grow{flex:1;min-width:0}
.nk-pill{display:inline-block;padding:2px 10px;border-radius:99px;background:var(--brand-soft);color:var(--brand)!important;font-weight:600;font-size:.78rem}
.nk-pill.sun{background:var(--sun-soft);color:var(--sun)!important}
.nk-stars{letter-spacing:2px;font-size:1.05rem}
.nk-bar{height:14px;border-radius:99px;background:var(--line);overflow:hidden}
.nk-bar>i{display:block;height:100%;border-radius:99px;background:linear-gradient(90deg,var(--sun),#ffcf6b)}
.nk-bar.brand>i{background:linear-gradient(90deg,var(--brand),#43c9c0)}
.nk-stats{display:flex;gap:8px}
.nk-stat{flex:1;background:var(--card);border:2px solid var(--line);border-radius:18px;padding:8px 6px;text-align:center}
.nk-stat b{display:block;font-family:'Baloo 2','Baloo Chettan 2','Noto Sans Malayalam',sans-serif;font-size:1.35rem;line-height:1.1}
.nk-stat span{font-size:.72rem;color:var(--muted)!important}
.nk-story{background:var(--card);border:2px solid var(--line);border-radius:26px;padding:22px 18px;text-align:center;box-shadow:var(--shadow)}
.nk-story .em{font-size:4.2rem;line-height:1.1}
.nk-story p{font-size:1.2rem;line-height:1.5;margin:10px 0 0;font-weight:500}
.nk-q{background:var(--card);border:2px solid var(--line);border-radius:22px;padding:16px 18px;font-size:1.15rem;font-weight:600;line-height:1.4}
.nk-fb{border-radius:16px;padding:12px 14px;font-weight:500;line-height:1.45}
.nk-fb.ok{background:var(--good-soft);color:var(--good)!important;border:2px solid var(--good)}
.nk-fb.no{background:var(--bad-soft);color:var(--bad)!important;border:2px solid var(--bad)}
.nk-fb.hint{background:var(--sun-soft);color:var(--ink)!important;border:2px solid var(--sun)}
.nk-fb *{color:inherit!important}
.nk-dots{display:flex;gap:6px;justify-content:center;flex-wrap:nowrap}
.nk-dot{width:13px;height:13px;border-radius:50%;background:var(--line);flex:none}
.nk-dot.on{background:var(--brand)}.nk-dot.cur{background:var(--sun)}
.nk-big{font-family:'Baloo 2','Baloo Chettan 2','Noto Sans Malayalam',sans-serif;font-size:2.4rem;font-weight:800;text-align:center;line-height:1.1}
.nk-big small{display:block;font-size:.8rem;color:var(--muted);font-weight:500;font-family:'Lexend','Noto Sans Malayalam',sans-serif}
.nk-money{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;min-height:42px}
.nk-money span{background:var(--sun-soft);border:2px solid var(--sun);border-radius:99px;padding:2px 10px;font-weight:600;font-size:.95rem}
.nk-jar{display:flex;align-items:center;gap:10px}
.nk-jar .bar{flex:1}
.nk-badge{background:var(--card);border:2px solid var(--line);border-radius:20px;padding:12px 6px;text-align:center}
.nk-badge .em{font-size:2rem}.nk-badge.locked{opacity:.4;filter:grayscale(1)}
.nk-badge b{display:block;font-size:.78rem;line-height:1.2;margin-top:2px}
.nk-badge span{font-size:.68rem;color:var(--muted)!important}
.nk-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.nk-table{width:100%;border-collapse:collapse;font-size:.9rem}
.nk-table td,.nk-table th{padding:6px 4px;border-bottom:1px solid var(--line);text-align:left}
.nk-table th{color:var(--muted);font-weight:600;font-size:.78rem}
.nk-foot b{color:inherit}
.nk-foot{font-size:.75rem;color:var(--muted)!important;text-align:center;margin-top:24px;line-height:1.5}
.nk-seg{display:flex;gap:6px}
.nk-seg b{flex:1;text-align:center;padding:6px 4px;border-radius:12px;background:var(--brand-soft);font-size:.8rem}
@keyframes pop{0%{transform:scale(.7);opacity:0}70%{transform:scale(1.08)}100%{transform:scale(1);opacity:1}}
.nk-pop{animation:pop .45s ease both}
@media (prefers-reduced-motion:reduce){.nk-pop{animation:none}.stButton>button{transition:none}}
"""


ML_CSS = ".stApp{line-height:1.75}.nk-title,.nk-q,.nk-story p{line-height:1.45!important}.stButton>button p{line-height:1.4;font-size:.9rem}[class*='st-key-ns-'] .stButton>button p{font-size:.78rem}[class*='st-key-ns-'] .stButton>button{padding-left:4px!important;padding-right:4px!important}.nk-hero p,.nk-hero .nk-sub{padding-right:52px}.nk-hero .nk-title{font-size:1.4rem}"


def inject(mode, lang="en"):
    extra = ML_CSS if lang == "ml" else ""
    st.markdown(f"<style>{theme_css(mode)}{BASE_CSS}{extra}</style>", unsafe_allow_html=True)


def esc(x):
    return html.escape(str(x), quote=True)


def md(s):
    """Render an HTML string (blank lines would break the block, so squeeze them)."""
    flat = "".join(line.strip() for line in s.strip().splitlines())
    st.markdown(flat, unsafe_allow_html=True)


def stars(n, total=3):
    return "★" * n + "☆" * (total - n)


def bar(pct, brand=False):
    pct = max(0, min(100, pct))
    return f'<div class="nk-bar{" brand" if brand else ""}"><i style="width:{pct:.0f}%"></i></div>'


def dots(n, cur, total):
    out = []
    for i in range(total):
        cls = "on" if i < n else ("cur" if i == cur else "")
        out.append(f'<span class="nk-dot {cls}"></span>')
    return f'<div class="nk-dots">{"".join(out)}</div>'


def inr(x):
    """Indian digit grouping: 1,23,456."""
    x = int(round(x))
    sign = "-" if x < 0 else ""
    s = str(abs(x))
    if len(s) <= 3:
        return f"{sign}₹{s}"
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return f"{sign}₹{','.join(parts)},{tail}"
'''

_SOURCES['voice'] = r'''"""Read-aloud. English and Malayalam use the browser voice by default.

For a natural Malayalam voice, add a Sarvam AI key (https://www.sarvam.ai). Set it in
.streamlit/secrets.toml (or the Streamlit Cloud "Secrets" box) or as an environment variable:

    SARVAM_API_KEY = "your-key"
    SARVAM_MODEL   = "bulbul:v4-flash" # optional
    SARVAM_SPEAKER = "shilpa_hi_narration"  # optional, must match the model
    SARVAM_PACE    = "1.0"            # optional

Audio is requested only when the Listen button is pressed, and each sentence is cached.
"""
import base64
import hashlib
import json
import os
import urllib.error
import urllib.request

import streamlit as st

from i18n import T, lang

SARVAM_URL = "https://api.sarvam.ai/text-to-speech"
LANG_CODE = {"en": "en-IN", "ml": "ml-IN"}


def _secret(name, default=""):
    value = None
    try:
        value = st.secrets.get(name)
    except Exception:
        value = None
    return str(value) if value else os.environ.get(name, default)


AUDIO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio", "ml")


def clip_name(text):
    """File name of a pre-made clip. make_audio.py uses the same function."""
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:16] + ".mp3"


def premade(text):
    path = os.path.join(AUDIO_DIR, clip_name(text))
    return path if os.path.isfile(path) else None


def sarvam_ready():
    return bool(_secret("SARVAM_API_KEY"))


@st.cache_data(show_spinner=False, max_entries=500, ttl=7 * 24 * 3600)
def _sarvam_audio(text, code, model, speaker, pace):
    """Returns WAV bytes. Raises on any failure, so failures are never cached."""
    key = _secret("SARVAM_API_KEY")
    if not key:
        raise RuntimeError("No Sarvam key")
    body = {"text": text[:1400], "target_language_code": code, "model": model, "speaker": speaker, "pace": pace,
            "speech_sample_rate": 24000}
    req = urllib.request.Request(
        SARVAM_URL, data=json.dumps(body).encode("utf-8"), method="POST",
        headers={"Content-Type": "application/json", "api-subscription-key": key})
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise RuntimeError("Sarvam %s: %s" % (exc.code, exc.read().decode("utf-8", "ignore")[:120]))
    return base64.b64decode(data["audios"][0])


def status():
    if sarvam_ready():
        err = st.session_state.get("voice_err")
        base = T("Malayalam voice: Sarvam is connected.")
        return base + (" " + T("Last problem: {err}", err=err) if err else "")
    if os.path.isdir(AUDIO_DIR) and os.listdir(AUDIO_DIR):
        return T("Malayalam voice: saved audio clips are installed.")
    return T("Malayalam voice: using the browser voice. Add a Sarvam key in the app secrets for a natural voice.")


LISTEN_HTML = """
<style>
html,body{margin:0;background:transparent;font-family:system-ui,'Noto Sans Malayalam',sans-serif}
button{display:inline-flex;gap:8px;align-items:center;min-height:40px;padding:0 16px;border-radius:99px;background:#F5A524;color:#3B2800;font-weight:700;font-size:14px;border:0;cursor:pointer;font-family:inherit}
button:focus-visible{outline:3px solid #0B7A75;outline-offset:2px}
#n{font-size:12px;color:#7a8b87;margin-top:4px}
</style>
<button id="b" type="button">__LABEL__</button><div id="n" hidden></div>
<script>
const T=__TEXT__, L=__LANG__, NOVOICE=__NOVOICE__, NOSPEECH=__NOSPEECH__;
document.getElementById('b').addEventListener('click',function(){
  const n=document.getElementById('n');
  try{
    const s=window.speechSynthesis;
    if(!s||!window.SpeechSynthesisUtterance){n.textContent=NOSPEECH;n.hidden=false;return}
    s.cancel();const u=new SpeechSynthesisUtterance(T);u.lang=L;u.rate=.9;
    const want=L.toLowerCase(),vs=s.getVoices()||[];
    const v=vs.find(function(x){return x.lang.replace('_','-').toLowerCase()===want})||vs.find(function(x){return x.lang.toLowerCase().indexOf(want.slice(0,2))===0});
    if(v){u.voice=v}else if(want.indexOf('ml')===0&&vs.length){n.textContent=NOVOICE;n.hidden=false;return}
    s.speak(u);
  }catch(e){}
});
</script>
"""


def _browser_widget(text, code):
    page = (LISTEN_HTML.replace("__LABEL__", "🔊 " + T("Listen"))
            .replace("__TEXT__", json.dumps(text))
            .replace("__LANG__", json.dumps(code))
            .replace("__NOVOICE__", json.dumps(T("No Malayalam voice on this device. A parent can add a natural voice in Parent corner.")))
            .replace("__NOSPEECH__", json.dumps(T("This browser cannot read aloud."))))
    if hasattr(st, "iframe"):
        st.iframe(page.strip(), height=70)
    else:  # Streamlit 1.41 to 1.5x
        import streamlit.components.v1 as components
        components.html(page, height=70)


def _play(text):
    st.session_state.voice_play = text


def listen(text, force=None):
    """Show a Listen control for text in the current language (or force='ml')."""
    ss = st.session_state
    which = force or lang()
    if which == "ml" and (sarvam_ready() or premade(text)):
        tag = hashlib.md5(text.encode("utf-8")).hexdigest()[:10]
        st.button("🔊 " + T("Listen"), key=f"listen-{tag}", on_click=_play, args=(text,))
        if ss.get("voice_play") == text:
            ss.voice_play = None            # play once, then clear
            try:
                clip = premade(text)
                if clip:                    # saved clip: no Sarvam call, no cost
                    with open(clip, "rb") as fh:
                        ss.voice_err = ""
                        st.audio(fh.read(), format="audio/mp3", autoplay=True)
                    return
                audio = _sarvam_audio(text, LANG_CODE["ml"], _secret("SARVAM_MODEL", "bulbul:v4-flash"),
                                      _secret("SARVAM_SPEAKER", "shilpa_hi_narration"), float(_secret("SARVAM_PACE", "1.0")))
                ss.voice_err = ""
                st.audio(audio, format="audio/wav", autoplay=True)
            except Exception as exc:       # fall back to the browser voice below
                ss.voice_err = str(exc)[:160]
                _browser_widget(text, LANG_CODE["ml"])
        return
    _browser_widget(text, LANG_CODE.get(which, "en-IN"))
'''

_SOURCES['activities'] = r'''"""Mini games. Every game has the signature game(lesson) -> bool (finished?).

State lives in st.session_state["act"], which the app resets for each lesson.
All money is practice money. Rates and prices are examples, not predictions.
"""
import random

import streamlit as st

from i18n import T
from ui import bar, esc, inr, md


def A():
    return st.session_state.act


# ----------------------------------------------------------------- helpers
def _set(field, value, seen_key=None):
    a = A()
    a[field] = value
    if seen_key:
        a.setdefault("seen", [])
        tag = "|".join(str(a.get(f)) for f in seen_key)
        if tag not in a["seen"]:
            a["seen"].append(tag)


def chips(name, options, current, fmt, field, seen_key=None):
    with st.container(key=f"ns-{name}"):
        cols = st.columns(len(options))
        for col, opt in zip(cols, options):
            with col:
                state = "sel" if opt == current else "opt"
                with st.container(key=f"{state}-{name}-{opt}"):
                    st.button(fmt(opt), key=f"b-{name}-{opt}", on_click=_set, args=(field, opt, seen_key))


def M(kind, key, **kw):
    """A message to show later. It stores the English key, so a language switch re-translates it."""
    return (kind, key, kw)


def feedback(kind, key, **kw):
    md(f'<div class="nk-fb {kind}">{esc(T(key, **kw))}</div>')


def show(msg, items=None):
    kind, key, kw = msg
    if key.startswith("@sort") and items is not None:
        why = items[kw["i"]][3]
        text = why if key == "@sortok" else T("Not quite. Think again.") + " " + why
        md(f'<div class="nk-fb {kind}">{esc(text)}</div>')
    else:
        feedback(kind, key, **kw)


def progress_hint(need, have, what):
    md(f'<div class="nk-sub" style="text-align:center">{T("{what}: {have} of {need}", what=T(what), have=min(have, need), need=need)}</div>')


# ----------------------------------------------------------------- coins
DENOMS = [1, 2, 5, 10, 20]


def _coin_add(v):
    a = A()
    a["coins"].append(v)
    a["msg"] = None


def _coin_undo():
    a = A()
    if a["coins"]:
        a["coins"].pop()
    a["msg"] = None


def _coin_clear():
    a = A()
    a["coins"] = []
    a["msg"] = None


def _coin_check(rounds):
    a = A()
    target = rounds[a["r"]]["target"]
    total = sum(a["coins"])
    if total == target:
        if a["r"] + 1 >= len(rounds):
            a["done"] = True
            a["msg"] = M("ok", "Perfect! You paid exactly the right amount.")
        else:
            a["r"] += 1
            a["coins"] = []
            a["msg"] = M("ok", "Yes! Exactly right. Here comes the next one.")
    elif total < target:
        a["msg"] = M("hint", "Not enough yet. You need {amt} more.", amt=inr(target - total))
    else:
        a["msg"] = M("no", "That is {amt} too much. Press Undo and try again.", amt=inr(total - target))


def coins(lesson):
    a = A()
    rounds = lesson["act"]["rounds"]
    a.setdefault("r", 0)
    a.setdefault("coins", [])
    a.setdefault("msg", None)
    rd = rounds[min(a["r"], len(rounds) - 1)]
    total = sum(a["coins"])
    chips_html = "".join(f"<span>{inr(c)}</span>" for c in a["coins"]) or f'<span style="opacity:.5">{esc(T("Tap coins and notes"))}</span>'
    md(f'<div class="nk-card"><div class="nk-big">{rd["item"]}<small>{esc(rd["say"])}</small>{inr(rd["target"])}</div></div>')
    md(f'<div class="nk-card"><div class="nk-money">{chips_html}</div><div class="nk-big" style="margin-top:6px">{inr(total)}<small>{esc(T("you have paid"))}</small></div></div>')
    if not a.get("done"):
        with st.container(key="ns-coin-row"):
            cols = st.columns(len(DENOMS))
            for col, d in zip(cols, DENOMS):
                with col:
                    with st.container(key=f"tile-coin-{d}"):
                        st.button(f"₹{d}", key=f"coin-{d}", on_click=_coin_add, args=(d,))
        with st.container(key="ns-coin-act"):
            c1, c2, c3 = st.columns([1, 1, 1.4])
            with c1:
                st.button(T("↩ Undo"), key="coin-undo", on_click=_coin_undo)
            with c2:
                st.button(T("Clear"), key="coin-clear", on_click=_coin_clear)
            with c3:
                st.button(T("Check ✓"), key="coin-check", type="primary", on_click=_coin_check, args=(rounds,))
    if a["msg"]:
        show(a["msg"])
    return bool(a.get("done"))


# ----------------------------------------------------------------- sort
def _sort_pick(items, idx):
    a = A()
    item = items[a["i"]]
    if idx == item[2]:
        a["msg"] = M("ok", "@sortok", i=a["i"])
        a["i"] += 1
        a["lastok"] = True
        if a["i"] >= len(items):
            a["done"] = True
    else:
        a["wrong"] += 1
        a["msg"] = M("hint", "@sortwrong", i=a["i"])


def sort(lesson):
    a = A()
    items, labels = lesson["act"]["items"], lesson["act"]["labels"]
    a.setdefault("i", 0)
    a.setdefault("wrong", 0)
    a.setdefault("msg", None)
    if not a.get("done"):
        it = items[a["i"]]
        md(f'<div class="nk-card" style="text-align:center"><div style="font-size:3.4rem;line-height:1.1">{it[0]}</div>'
           f'<div class="nk-title" style="margin-top:6px">{esc(it[1])}</div>'
           f'<div class="nk-sub">{esc(T("Item {n} of {total}. Where does it belong?", n=a["i"] + 1, total=len(items)))}</div></div>')
        n = len(labels)
        per_row = 2 if n > 2 else n
        for r in range(0, n, per_row):
            with st.container(key=f"ns-sortrow-{r}"):
                cols = st.columns(per_row)
                for col, k in zip(cols, range(r, min(r + per_row, n))):
                    with col:
                        with st.container(key=f"tile-sort-{k}"):
                            st.button(labels[k], key=f"sort-{a['i']}-{k}", on_click=_sort_pick, args=(items, k))
    if a["msg"]:
        show(a["msg"], items)
    if a.get("done"):
        key = "All sorted! You made {n} slip." if a["wrong"] == 1 else "All sorted! You made {n} slips."
        md(f'<div class="nk-fb ok nk-pop">{esc(T(key, n=a["wrong"]))}</div>')
    return bool(a.get("done"))


# ----------------------------------------------------------------- piggy
def _piggy_save(step, goal):
    a = A()
    a["amount"] = min(goal, a["amount"] + step)
    a["n"] += 1
    if a["amount"] >= goal:
        a["done"] = True


def piggy(lesson):
    a = A()
    cfg = lesson["act"]
    a.setdefault("amount", 0)
    a.setdefault("n", 0)
    pct = a["amount"] / cfg["goal"] * 100
    md(f'<div class="nk-card"><div class="nk-big">{cfg["item"]} 🐷<small>{esc(T("Goal: a {what} for {amt}", what=cfg["what"], amt=inr(cfg["goal"])))}</small>'
       f'{inr(a["amount"])}</div><div style="margin-top:10px">{bar(pct)}</div>'
       f'<div class="nk-sub" style="text-align:center;margin-top:6px">{esc(cfg["unit"])} {a["n"]}</div></div>')
    if not a.get("done"):
        st.button(T("Save {amt} this {unit} 🪙", amt=inr(cfg["step"]), unit=cfg["unit"].lower()), key="piggy-save", type="primary",
                  on_click=_piggy_save, args=(cfg["step"], cfg["goal"]))
        st.caption(T("Small, regular steps reach the goal."))
    else:
        unit_pl = cfg.get("unit_pl") or cfg["unit"].lower() + "s"
        feedback("ok", "You reached {goal} in {n} {units} by saving {step} each time. Patience paid off!",
                 goal=inr(cfg["goal"]), n=a["n"], units=unit_pl, step=inr(cfg["step"]))
    return bool(a.get("done"))


# ----------------------------------------------------------------- allocate (jars, budget)
def _alloc_move(key, delta, step, total):
    a = A()
    cur = a["vals"][key]
    left = total - sum(a["vals"].values())
    if delta > 0 and left < step:
        return
    a["vals"][key] = max(0, cur + delta * step)
    a["msg"] = None


def _alloc_check(cfg):
    a = A()
    v, total = a["vals"], cfg["total"]
    left = total - sum(v.values())
    if left != 0:
        a["msg"] = M("hint", "You still have {amt} to place. Every rupee needs a job.", amt=inr(left))
        return
    if cfg["kind"] == "jars":
        if any(x == 0 for x in v.values()):
            a["msg"] = M("hint", "Give every jar at least a little. Even Share and Save matter.")
        elif v["save"] < total * 0.2:
            a["msg"] = M("hint", "Try to save at least a fifth of your money. Future you will say thanks!")
        else:
            a["done"] = True
            a["msg"] = M("ok", "Nice split. Every jar has a job and your savings are growing.")
    else:
        if v["school"] < total * 0.25:
            a["msg"] = M("hint", "Needs come first. Give School things at least a quarter of your money.")
        elif v["save"] < total * 0.1:
            a["msg"] = M("hint", "Add at least a tenth to Savings, so you can handle surprises.")
        elif v["snacks"] + v["fun"] > total * 0.5:
            a["msg"] = M("hint", "Snacks and Fun together are more than half. Can you trim a little?")
        else:
            a["done"] = True
            a["msg"] = M("ok", "A balanced budget! Needs first, then savings, then fun.")


def alloc(lesson):
    a = A()
    cfg = lesson["act"]
    total, step = cfg["total"], cfg["step"]
    a.setdefault("vals", {k: 0 for k, _ in cfg["cats"]})
    a.setdefault("msg", None)
    left = total - sum(a["vals"].values())
    md(f'<div class="nk-card"><div class="nk-big">{inr(left)}<small>{esc(T("left to place out of {total}", total=inr(total)))}</small></div></div>')
    for key, label in cfg["cats"]:
        pct = a["vals"][key] / total * 100
        with st.container(key=f"card-alloc-{key}"):
            with st.container(key=f"ns-alloc-{key}"):
                c1, c2, c3 = st.columns([3, 1, 1])
                with c1:
                    md(f'<div class="nk-title" style="font-size:1.05rem">{esc(label)}</div><div class="nk-sub">{inr(a["vals"][key])}</div>{bar(pct, True)}')
                with c2:
                    st.button("−", key=f"al-m-{key}", on_click=_alloc_move, args=(key, -1, step, total), disabled=a.get("done", False))
                with c3:
                    st.button("+", key=f"al-p-{key}", on_click=_alloc_move, args=(key, 1, step, total), disabled=a.get("done", False))
    if not a.get("done"):
        st.button(T("Check my plan ✓"), key="alloc-check", type="primary", on_click=_alloc_check, args=(cfg,))
    if a["msg"]:
        show(a["msg"])
    return bool(a.get("done"))


# ----------------------------------------------------------------- stall (profit)
def _stall_new_day(days):
    a = A()
    a["day"] = random.randrange(len(days))
    a["result"] = None


def _stall_price(delta, lo, hi):
    a = A()
    a["price"] = max(lo, min(hi, a["price"] + delta))


def _demand(cfg, price, mult):
    return max(0, round((cfg["base"] - cfg["slope"] * (price - cfg["start"])) * mult))


def _stall_run(cfg):
    a = A()
    mult = cfg["days"][a["day"]][2]
    price = a["price"]
    sold = _demand(cfg, price, mult)
    income, costs = sold * price, sold * cfg["cost"]
    profit = income - costs
    goal = round(cfg["target"] * mult / 10) * 10
    lo = hi = None
    for p in range(cfg["pmin"], cfg["pmax"] + 1):
        if (p - cfg["cost"]) * _demand(cfg, p, mult) >= goal:
            lo = p if lo is None else lo
            hi = p
    a["runs"] += 1
    a["result"] = dict(sold=sold, income=income, costs=costs, profit=profit, goal=goal, lo=lo, hi=hi, price=price)
    if profit >= goal or a["runs"] >= 4:
        a["done"] = True
        a["won"] = profit >= goal


def stall(lesson):
    a = A()
    cfg = lesson["act"]
    days = cfg["days"]
    if "day" not in a:
        a["day"] = 0
        a["price"] = cfg["start"]
        a["runs"] = 0
        a["result"] = None
    name, emoji, mult = days[a["day"]]
    goal = round(cfg["target"] * mult / 10) * 10
    md(f'<div class="nk-card" style="text-align:center"><div class="nk-big">{emoji}<small>{esc(T("{name} at the {product} stall. Each {unit} costs {cost} to make.", name=name, product=cfg["product"], unit=cfg["unit"], cost=inr(cfg["cost"])))}</small></div>'
       f'<div class="nk-sub" style="margin-top:6px">{T("Goal today: a profit of at least <b>{goal}</b> (try {n} of 4)", goal=inr(goal), n=min(a["runs"] + 1, 4))}</div></div>')
    md(f'<div class="nk-card"><div class="nk-big">{inr(a["price"])}<small>{esc(T("price per {unit}", unit=cfg["unit"]))}</small></div></div>')
    s1, s2 = cfg["steps"]
    with st.container(key="ns-stall-price"):
        cols = st.columns(4)
        for col, d in zip(cols, [-s2, -s1, s1, s2]):
            with col:
                st.button(("+" if d > 0 else "−") + str(abs(d)), key=f"stall-p{d}", on_click=_stall_price,
                          args=(d, cfg["pmin"], cfg["pmax"]), disabled=bool(a.get("done")))
    res = a["result"]
    if not a.get("done"):
        st.button(T("Open the stall ({emoji})", emoji=emoji), key="stall-run", type="primary", on_click=_stall_run, args=(cfg,))
    if res:
        md(f'<div class="nk-card"><table class="nk-table"><tr><th>{esc(T("Sold"))}</th><th>{esc(T("Money in"))}</th><th>{esc(T("Costs"))}</th><th>{esc(T("Profit"))}</th></tr>'
           f'<tr><td>{res["sold"]}</td><td>{inr(res["income"])}</td><td>{inr(res["costs"])}</td><td><b>{inr(res["profit"])}</b></td></tr></table></div>')
        if res["profit"] >= res["goal"]:
            feedback("ok", "Goal reached! Profit is what is left after costs, and you found a price customers like.")
        elif res["profit"] < 0:
            feedback("no", "A loss. You paid more to make the goods than you earned. Raise the price a little.")
        elif res["sold"] == 0:
            feedback("hint", "Nobody bought anything. That price is too high. Try lowering it.")
        elif res["lo"] is not None:
            feedback("hint", "Close. On a day like this, prices between {lo} and {hi} reach the goal.", lo=inr(res["lo"]), hi=inr(res["hi"]))
        else:
            feedback("hint", "This is a tough day. Do your best price, then try another day.")
        if a.get("done") and not a.get("won"):
            feedback("hint", "That is 4 tries. Real shopkeepers keep adjusting too. Let us move on to the quiz.")
    if res and not a.get("done"):
        st.button(T("Try another day ➜"), key="stall-next", on_click=_stall_new_day, args=(days,))
    return bool(a.get("done"))


# ----------------------------------------------------------------- order
def _order_pick(idx, n):
    a = A()
    if idx == len(a["placed"]):
        a["placed"].append(idx)
        a["msg"] = M("ok", "Yes!")
        if len(a["placed"]) == n:
            a["done"] = True
            a["msg"] = M("ok", "All in the right order. Safe paying habit unlocked!")
    else:
        a["wrong"] += 1
        a["msg"] = M("hint", "Not that one yet. What happens first, before money moves?")


def order(lesson):
    a = A()
    cfg = lesson["act"]
    steps = cfg["steps"]
    if "shuffled" not in a:
        s = list(range(len(steps)))
        for _ in range(10):
            random.shuffle(s)
            if s != sorted(s):
                break
        a["shuffled"], a["placed"], a["wrong"], a["msg"] = s, [], 0, None
    md(f'<div class="nk-title" style="text-align:center">{esc(cfg["title"])}</div>')
    placed = "".join(f'<tr><td><b>{i + 1}</b></td><td>{esc(t)}</td></tr>' for i, k in enumerate(a["placed"]) for t in [steps[k]]) or f'<tr><td colspan="2" class="nk-sub">{esc(T("Tap the steps below in order"))}</td></tr>'
    md(f'<div class="nk-card"><table class="nk-table">{placed}</table></div>')
    if not a.get("done"):
        for k in [x for x in a["shuffled"] if x not in a["placed"]]:
            st.button(steps[k], key=f"ord-{k}", on_click=_order_pick, args=(k, len(steps)))
    if a["msg"]:
        show(a["msg"])
    return bool(a.get("done"))


# ----------------------------------------------------------------- compound growth
def fv(monthly, rate, years):
    r = rate / 1200
    n = years * 12
    if r == 0:
        return monthly * n
    return monthly * (((1 + r) ** n - 1) / r) * (1 + r)


def grow(lesson):
    a = A()
    a.setdefault("monthly", 1000)
    a.setdefault("rate", 8)
    a.setdefault("years", 10)
    a.setdefault("seen", ["10"])
    md(f'<div class="nk-sub">{esc(T("Monthly saving"))}</div>')
    chips("gm", [500, 1000, 2000, 5000], a["monthly"], inr, "monthly")
    md(f'<div class="nk-sub">{esc(T("Example yearly growth (not a promise)"))}</div>')
    chips("gr", [6, 8, 12], a["rate"], lambda x: f"{x}%", "rate")
    md(f'<div class="nk-sub">{esc(T("Years"))}</div>')
    chips("gy", [5, 10, 15, 20, 30], a["years"], str, "years", seen_key=["years"])
    put = a["monthly"] * 12 * a["years"]
    val = fv(a["monthly"], a["rate"], a["years"])
    later = fv(a["monthly"], a["rate"], max(0, a["years"] - 5))
    md(f'<div class="nk-card"><div class="nk-big">{inr(val)}<small>{esc(T("after {years} years", years=a["years"]))}</small></div>'
       f'<div class="nk-sub" style="margin-top:8px">{esc(T("You put in {amt}", amt=inr(put)))}</div>{bar(put / val * 100, True)}'
       f'<div class="nk-sub" style="margin-top:6px">{esc(T("Growth on growth: {amt}", amt=inr(val - put)))}</div>{bar((val - put) / val * 100)}</div>')
    if a["years"] > 5:
        md(f'<div class="nk-fb hint">{esc(T("Start 5 years later and the same saving grows to only {amt}. Starting early is a superpower.", amt=inr(later)))}</div>')
    seen = len(set(a["seen"]))
    if seen >= 3:
        a["done"] = True
    else:
        progress_hint(3, seen, "Try different years. Years tried")
    md(f'<div class="nk-sub" style="text-align:center">{esc(T("Example only. Real returns go up and down and are never guaranteed."))}</div>')
    return bool(a.get("done"))


# ----------------------------------------------------------------- practice market
COMPANIES = [
    ("chai", "☕", "Chintu Chai Co.", "Steady seller"),
    ("rocket", "🚀", "Rocket Phones", "Wild swings"),
    ("rick", "🛺", "Green Rickshaw", "Medium swings"),
    ("banana", "🍌", "Kerala Bananas", "Steady seller"),
]
YEARS = [
    ("Boom year", {"chai": 6, "rocket": 45, "rick": 18, "banana": 5}),
    ("Crash year", {"chai": 1, "rocket": -35, "rick": -12, "banana": 2}),
    ("Normal year", {"chai": 4, "rocket": 8, "rick": 7, "banana": 3}),
]
MARKET_UNIT = 1000
MARKET_TOTAL = 10000


def _mkt_move(key, delta):
    a = A()
    left = MARKET_TOTAL - sum(a["vals"].values())
    if delta > 0 and left < MARKET_UNIT:
        return
    a["vals"][key] = max(0, a["vals"][key] + delta * MARKET_UNIT)
    a["ran"] = []
    a["last"] = None


def _mkt_run(i):
    a = A()
    name, rets = YEARS[i]
    value = sum(v * (1 + rets[k] / 100) for k, v in a["vals"].items())
    a["last"] = (name, rets, value)
    if i not in a["ran"]:
        a["ran"].append(i)
    if len(a["ran"]) == len(YEARS):
        a["done"] = True


def market(lesson):
    a = A()
    a.setdefault("vals", {k: 0 for k, *_ in COMPANIES})
    a.setdefault("ran", [])
    a.setdefault("last", None)
    left = MARKET_TOTAL - sum(a["vals"].values())
    md(f'<div class="nk-card"><div class="nk-big">{inr(left)}<small>{esc(T("practice money left to place (made-up companies)"))}</small></div></div>')
    for key, em, name, note in COMPANIES:
        with st.container(key=f"card-mk-{key}"):
            with st.container(key=f"ns-mk-{key}"):
                c1, c2, c3 = st.columns([3, 1, 1])
                with c1:
                    md(f'<div class="nk-title" style="font-size:1rem">{em} {esc(T(name))}</div><div class="nk-sub">{esc(T(note))} · {inr(a["vals"][key])}</div>')
                with c2:
                    st.button("−", key=f"mk-m-{key}", on_click=_mkt_move, args=(key, -1))
                with c3:
                    st.button("+", key=f"mk-p-{key}", on_click=_mkt_move, args=(key, 1))
    ready = left == 0
    if not ready:
        md(f'<div class="nk-sub" style="text-align:center">{esc(T("Place all your practice money to start the years."))}</div>')
    with st.container(key="ns-mk-years"):
        cols = st.columns(len(YEARS))
        for i, col in enumerate(cols):
            with col:
                st.button(T(YEARS[i][0]), key=f"mk-y{i}", on_click=_mkt_run, args=(i,), disabled=not ready)
    if a["last"]:
        name, rets, value = a["last"]
        change = value - MARKET_TOTAL
        rows = "".join(f'<tr><td>{em} {esc(T(nm))}</td><td>{rets[k]:+d}%</td></tr>' for k, em, nm, _ in COMPANIES)
        kind = "ok" if change >= 0 else "no"
        md(f'<div class="nk-card"><div class="nk-title">{esc(T(name))}</div><table class="nk-table"><tr><th>{esc(T("Company"))}</th><th>{esc(T("Year result"))}</th></tr>{rows}</table></div>')
        feedback(kind, "Your practice money is now {value} ({change}).", value=inr(value), change=("+" if change >= 0 else "−") + inr(abs(change)))
    if a.get("done"):
        spread = sum(1 for v in a["vals"].values() if v > 0)
        if spread >= 3:
            feedback("hint", "You spread your money across several companies, so no single bad year hurt too much. That is diversification.")
        else:
            feedback("hint", "Your money sat in few companies, so results swung more. Spreading across more companies usually smooths the ride.")
    else:
        progress_hint(len(YEARS), len(a["ran"]), "Years played")
    md(f'<div class="nk-sub" style="text-align:center">{esc(T("Made-up companies and made-up years. This is a learning game, never advice to buy anything."))}</div>')
    return bool(a.get("done"))


# ----------------------------------------------------------------- inflation
def inflation(lesson):
    a = A()
    a.setdefault("years", 10)
    a.setdefault("rate", 6)
    a.setdefault("seen", ["10|6"])
    md(f'<div class="nk-sub">{esc(T("Years from now"))}</div>')
    chips("iy", [5, 10, 20, 30], a["years"], str, "years", seen_key=["years", "rate"])
    md(f'<div class="nk-sub">{esc(T("Example yearly price rise"))}</div>')
    chips("ir", [4, 6, 8], a["rate"], lambda x: f"{x}%", "rate", seen_key=["years", "rate"])
    idle_txt = T("₹100 kept idle will then buy only this much of today's snack:")
    cost = 100 * (1 + a["rate"] / 100) ** a["years"]
    buys = 100 / (1 + a["rate"] / 100) ** a["years"]
    md(f'<div class="nk-card"><div class="nk-big">🍿 {inr(cost)}<small>{esc(T("what a ₹100 snack costs in {years} years", years=a["years"]))}</small></div>'
       f'<div class="nk-sub" style="margin-top:8px">{esc(idle_txt)}</div>{bar(buys)}'
       f'<div class="nk-sub" style="margin-top:4px">{T("<b>{pct}%</b> of it", pct=f"{buys:.0f}")}</div></div>')
    seen = len(set(a["seen"]))
    if seen >= 3:
        a["done"] = True
    else:
        progress_hint(3, seen, "Try other settings. Combinations tried")
    md(f'<div class="nk-sub" style="text-align:center">{esc(T("Example rates for learning. Real inflation changes from year to year."))}</div>')
    return bool(a.get("done"))


# ----------------------------------------------------------------- loan
def emi(principal, rate, years):
    r = rate / 1200
    n = years * 12
    if r == 0:
        return principal / n
    return principal * r * (1 + r) ** n / ((1 + r) ** n - 1)


def loan(lesson):
    a = A()
    a.setdefault("principal", 50000)
    a.setdefault("rate", 12)
    a.setdefault("years", 3)
    a.setdefault("seen", ["50000|12|3"])
    keys = ["principal", "rate", "years"]
    md(f'<div class="nk-sub">{esc(T("Amount borrowed"))}</div>')
    chips("lp", [20000, 50000, 100000], a["principal"], inr, "principal", seen_key=keys)
    md(f'<div class="nk-sub">{esc(T("Example yearly interest rate"))}</div>')
    chips("lr", [8, 12, 24], a["rate"], lambda x: f"{x}%", "rate", seen_key=keys)
    md(f'<div class="nk-sub">{esc(T("Years to repay"))}</div>')
    chips("ly", [1, 2, 3, 5], a["years"], str, "years", seen_key=keys)
    m = emi(a["principal"], a["rate"], a["years"])
    total = m * a["years"] * 12
    extra = total - a["principal"]
    md(f'<div class="nk-card"><div class="nk-big">{inr(m)}<small>{esc(T("EMI, paid every month"))}</small></div>'
       f'<table class="nk-table" style="margin-top:8px"><tr><td>{esc(T("You borrow"))}</td><td><b>{inr(a["principal"])}</b></td></tr>'
       f'<tr><td>{esc(T("You pay back"))}</td><td><b>{inr(total)}</b></td></tr>'
       f'<tr><td>{esc(T("Extra cost (interest)"))}</td><td><b>{inr(extra)}</b></td></tr></table>'
       f'<div style="margin-top:8px">{bar(extra / total * 100)}</div><div class="nk-sub">{esc(T("{pct}% of what you pay is interest", pct=f"{extra / total * 100:.0f}"))}</div></div>')
    seen = len(set(a["seen"]))
    if seen >= 3:
        a["done"] = True
    else:
        progress_hint(3, seen, "Try other settings. Combinations tried")
    md(f'<div class="nk-sub" style="text-align:center">{esc(T("Example only. Borrow from trusted, regulated lenders and ask a grown-up first."))}</div>')
    return bool(a.get("done"))


ENGINES = {
    "coins": coins, "sort": sort, "piggy": piggy, "alloc": alloc, "stall": stall, "order": order,
    "grow": grow, "market": market, "inflation": inflation, "loan": loan,
}


def play(lesson):
    return ENGINES[lesson["act"]["type"]](lesson)
'''


_HERE = _os.path.dirname(_os.path.abspath(__file__))
for _name in ('more_data_seed', 'more_data', 'content', 'storage', 'ml_ui', 'ml_lessons', 'ml_bank_seed', 'ml_bank_explore', 'ml_bank_pioneer', 'i18n', 'ui', 'voice', 'activities'):
    _bid = _hl.md5(_SOURCES[_name].encode('utf-8')).hexdigest()
    if getattr(_sys.modules.get(_name), '_ef_build', None) != _bid:
        _mod = _types.ModuleType(_name)
        _mod._ef_build = _bid
        _mod.__file__ = _os.path.join(_HERE, _name + ".py")
        _sys.modules[_name] = _mod
        exec(compile(_SOURCES[_name], _mod.__file__, "exec"), _mod.__dict__)

# ===== APP =====
# EasyFin, powered by NYZTrade: money learning for ages 5 to 14.  Run:  streamlit run app.py
#
# Practice money only. No real trading, no tips, no advice.
import datetime
import random
import time

import streamlit as st

import activities
import content as C
import i18n
import storage
import ui
import voice
from i18n import T
from ui import esc, inr, md

st.set_page_config(page_title="EasyFin | powered by NYZTrade", page_icon="🐿️", layout="centered", initial_sidebar_state="collapsed")

THEMES = ["auto", "light", "dark"]
THEME_LABEL = {"auto": "🌓 Auto", "light": "☀️ Light", "dark": "🌙 Dark"}   # shown through T()

GLOBAL_BADGES = [
    ("first", "First Step", "🌟", "Finish your first lesson"),
    ("five", "High Five", "🖐️", "Finish 5 lessons"),
    ("streak3", "On Fire", "🔥", "Learn 3 days in a row"),
    ("perfect", "Perfect Round", "💯", "Get every quiz question right first time"),
    ("xp500", "Power Up", "⚡", "Earn 500 XP"),
    ("whiz", "Quiz Whiz", "🧠", "Score 10 out of 10 in a Quick Quiz"),
    ("g_seed", "Seedling Graduate", "🌱", "Finish every Seedlings lesson"),
    ("g_explore", "Explorer Graduate", "🧭", "Finish every Explorers lesson"),
    ("g_pioneer", "Pioneer Graduate", "🚀", "Finish every Pioneers lesson"),
    ("all", "Money Master", "👑", "Finish all 22 lessons"),
]


# ------------------------------------------------------------------ state
def init():
    ss = st.session_state
    if "lang" not in ss:   # sessions opened before the Malayalam update have no language yet
        _l = storage.settings().get("lang", "en")
        ss.lang = _l if _l in ("en", "ml") else "en"
    if "boot" in ss:
        return
    ss.boot = True
    s = storage.settings()
    ss.theme = s["theme"] if s["theme"] in THEMES else "auto"
    ss.listen = bool(s["listen"])
    ss.lang = s.get("lang", "en") if s.get("lang") in ("en", "ml") else "en"
    ss.name = None
    ss.P = None
    ss.page = "learn"
    ss.lesson = None
    ss.stage = "story"
    ss.step = 0
    ss.act = {}
    ss.quiz = None
    ss.parent_ok = False
    ss.confirm_reset = False
    ss.err = ""
    ss.tick = time.time()
    ss.pick_band = "seed"
    ss.quick_band = "seed"


def commit():
    ss = st.session_state
    if ss.name and ss.P is not None:
        storage.save_profile(ss.name, ss.P)


def save_settings():
    ss = st.session_state
    storage.save_settings({"theme": ss.theme, "listen": ss.listen, "lang": ss.lang, "last_profile": ss.name or ""})


def tick():
    ss = st.session_state
    now = time.time()
    if ss.P is not None:
        ss.P["seconds"] += int(min(now - ss.tick, 90))
    ss.tick = now


def level(xp):
    return xp // 100 + 1, xp % 100


def total_stars(P):
    return sum(P["done"].values())


def touch_day(P):
    today = datetime.date.today()
    last = P["last_day"]
    if last == today.isoformat():
        return
    if last == (today - datetime.timedelta(days=1)).isoformat():
        P["streak"] += 1
    else:
        P["streak"] = 1
    P["last_day"] = today.isoformat()


def award(P, bid, new):
    if bid not in P["badges"]:
        P["badges"].append(bid)
        new.append(bid)


def check_badges(P, perfect=False, whiz=False):
    new = []
    done = P["done"]
    if len(done) >= 1:
        award(P, "first", new)
    if len(done) >= 5:
        award(P, "five", new)
    if P["streak"] >= 3:
        award(P, "streak3", new)
    if perfect:
        award(P, "perfect", new)
    if P["xp"] >= 500:
        award(P, "xp500", new)
    if whiz:
        award(P, "whiz", new)
    for b in C.BANDS:
        if all(l["id"] in done for l in C.lessons_for(b["id"])):
            award(P, "g_" + b["id"], new)
    if len(done) == len(C.LESSONS):
        award(P, "all", new)
    return new


def badge_info(bid):
    if bid.startswith("L:"):
        l = i18n.lesson(bid[2:])
        return l["badge"][0], l["badge"][1], T('Finish "{title}"', title=l["title"])
    for gid, name, em, desc in GLOBAL_BADGES:
        if gid == bid:
            return T(name), em, T(desc)
    return bid, "🏅", ""


# ------------------------------------------------------------------ callbacks
def go(page):
    ss = st.session_state
    ss.page = page
    ss.lesson = None
    ss.quiz = None
    ss.act = {}
    if page != "parent":
        ss.parent_ok = False


def cycle_theme():
    ss = st.session_state
    ss.theme = THEMES[(THEMES.index(ss.theme) + 1) % len(THEMES)]
    save_settings()


def toggle_lang():
    ss = st.session_state
    ss.lang = "ml" if ss.lang == "en" else "en"
    save_settings()


def toggle_listen():
    st.session_state.listen = not st.session_state.listen
    save_settings()


def set_band(band):
    ss = st.session_state
    ss.P["band"] = band
    commit()


def start_profile():
    ss = st.session_state
    nick = (ss.get("nick") or "").strip()[:20]
    if not nick:
        ss.err = "Please type a nickname."   # translated when shown
        return
    if not ss.get("consent"):
        ss.err = "A parent or guardian needs to be with you. Tick the box when they are."   # translated when shown
        return
    ss.err = ""
    open_profile(nick, ss.pick_band)


def open_profile(nick, band=None):
    ss = st.session_state
    ss.name = nick
    ss.P = storage.load_profile(nick)
    if band and not ss.P["done"] and ss.P["xp"] == 0:
        ss.P["band"] = band
    ss.tick = time.time()
    commit()
    save_settings()
    ss.page = "learn"


def switch_child():
    ss = st.session_state
    ss.name, ss.P, ss.lesson, ss.quiz, ss.parent_ok = None, None, None, None, False
    ss.act = {}


def open_lesson(lid):
    ss = st.session_state
    ss.lesson, ss.stage, ss.step, ss.act, ss.quiz = lid, "story", 0, {}, None


def story_move(delta, n):
    ss = st.session_state
    ss.step += delta
    if ss.step >= n:
        ss.stage = "game"
        ss.step = 0
    ss.step = max(0, ss.step)


def to_quiz(lid):
    ss = st.session_state
    ss.stage = "quiz"
    refs = [(lid, i) for i in range(len(C.LESSON_BY_ID[lid]["bank"]))]
    ss.quiz = build_quiz("lesson", refs, C.QUESTIONS_PER_PLAY, lid)


def band_refs(band):
    return [(l["id"], i) for l in C.lessons_for(band) for i in range(len(l["bank"]))]


def build_quiz(kind, refs, n, lid=None):
    """Questions are stored as (lesson id, bank index, option order), so the text can switch language live."""
    qs = []
    for lid_, idx in random.sample(refs, min(n, len(refs))):
        raw = C.LESSON_BY_ID[lid_]["bank"][idx]
        order = list(range(len(raw[1])))
        random.shuffle(order)
        qs.append(dict(lid=lid_, idx=idx, order=order, right=order.index(raw[2])))
    return dict(kind=kind, lid=lid, qs=qs, i=0, wrong=[], answered=False, first_ok=0, xp=0, result=None)


def pick(oi):
    ss = st.session_state
    qz = ss.quiz
    q = qz["qs"][qz["i"]]
    if qz["answered"] or oi in qz["wrong"]:
        return
    if oi == q["right"]:
        first = not qz["wrong"]
        qz["answered"] = True
        ss.P["q_total"] += 1
        gain = 10 if first else 5
        if first:
            qz["first_ok"] += 1
            ss.P["q_first"] += 1
        ss.P["xp"] += gain
        qz["xp"] += gain
        commit()
    else:
        qz["wrong"].append(oi)


def next_q():
    ss = st.session_state
    qz = ss.quiz
    if qz["i"] + 1 < len(qz["qs"]):
        qz["i"] += 1
        qz["wrong"], qz["answered"] = [], False
    else:
        finish_quiz()


def finish_quiz():
    ss = st.session_state
    qz, P = ss.quiz, ss.P
    n = len(qz["qs"])
    touch_day(P)
    if qz["kind"] == "lesson":
        lid = qz["lid"]
        stars_ = 3 if qz["first_ok"] >= n - 1 else (2 if qz["first_ok"] >= n - 2 else 1)
        bonus = 20 + 10 * stars_
        P["xp"] += bonus
        qz["xp"] += bonus
        P["done"][lid] = max(P["done"].get(lid, 0), stars_)
        P["lessons_played"] += 1
        new = []
        award(P, "L:" + lid, new)
        new += check_badges(P, perfect=qz["first_ok"] == n)
        qz["result"] = dict(stars=stars_, bonus=bonus, new=new)
    else:
        band = ss.quick_band
        bonus = 20 if qz["first_ok"] >= 8 else 5
        P["xp"] += bonus
        qz["xp"] += bonus
        P["quick_best"][band] = max(P["quick_best"].get(band, 0), qz["first_ok"])
        new = check_badges(P, whiz=qz["first_ok"] == n)
        qz["result"] = dict(stars=0, bonus=bonus, new=new)
    commit()


def start_quick():
    ss = st.session_state
    ss.quiz = build_quiz("quick", band_refs(ss.quick_band), C.QUICK_QUIZ_LENGTH)


def pick_quick_band(b):
    st.session_state.quick_band = b
    st.session_state.quiz = None


def pick_onboard_band(b):
    st.session_state.pick_band = b


def check_gate():
    ss = st.session_state
    try:
        ok = int(str(ss.get("gate", "")).strip()) == ss.gate_answer
    except ValueError:
        ok = False
    ss.parent_ok = ok
    ss.err = "" if ok else "That is not right. Try again."   # translated when shown


def lock_parent():
    st.session_state.parent_ok = False


def ask_reset():
    st.session_state.confirm_reset = True


def do_reset():
    ss = st.session_state
    storage.delete_profile(ss.name)
    ss.confirm_reset = False
    switch_child()


def cancel_reset():
    st.session_state.confirm_reset = False


# ------------------------------------------------------------------ shared UI
def band_buttons(current, on_pick, prefix):
    with st.container(key=f"ns-{prefix}-bands"):
        cols = st.columns(len(C.BANDS))
        for col, b in zip(cols, i18n.bands()):
            with col:
                state = "tab-on" if b["id"] == current else "tab"
                with st.container(key=f"{state}-{prefix}-{b['id']}"):
                    st.button(f'{b["name"]}\n{b["ages_short"]}', key=f"{prefix}-{b['id']}", on_click=on_pick, args=(b["id"],))


def topbar():
    ss = st.session_state
    with st.container(key="ns-top"):
        c1, c2, c3 = st.columns([2.1, 1.25, 1.1])
        with c1:
            md('<div class="nk-row"><span style="font-size:1.8rem">🐿️</span><div><div class="nk-title" style="font-size:1.1rem;white-space:nowrap">EasyFin</div><div class="nk-sub" style="margin:0;white-space:nowrap">powered by <b>NYZTrade</b></div></div></div>')
        with c2:
            st.button("English" if ss.lang == "ml" else "മലയാളം", key="lang-btn", on_click=toggle_lang)
        with c3:
            st.button(T(THEME_LABEL[ss.theme]), key="theme-btn", on_click=cycle_theme)


def nav():
    ss = st.session_state
    items = [("learn", "🎒 Learn"), ("quick", "⚡ Quiz"), ("rewards", "🏆 Rewards"), ("parent", "👪 Parent")]
    with st.container(key="ns-nav"):
        cols = st.columns(len(items))
        for col, (pid, label) in zip(cols, items):
            with col:
                state = "tab-on" if ss.page == pid else "tab"
                with st.container(key=f"{state}-nav-{pid}"):
                    st.button(T(label), key=f"nav-{pid}", on_click=go, args=(pid,))


def stats_row(P):
    lv, into = level(P["xp"])
    md(f'<div class="nk-stats">'
       f'<div class="nk-stat"><b>⭐ {total_stars(P)}</b><span>{esc(T("stars"))}</span></div>'
       f'<div class="nk-stat"><b>🔥 {P["streak"]}</b><span>{esc(T("day streak"))}</span></div>'
       f'<div class="nk-stat"><b>⚡ {P["xp"]}</b><span>XP</span></div>'
       f'<div class="nk-stat"><b>{esc(T("Lv {lv}", lv=lv))}</b><span>{esc(T("level"))}</span></div></div>')


def footer():
    md(f'<div class="nk-foot">{esc(T("Practice money only. EasyFin teaches ideas and habits. It gives no investment advice or tips, and no real money moves here. Examples use made-up numbers."))}'
       '<br><b>EasyFin</b> · powered by <b>NYZTrade</b></div>')


# ------------------------------------------------------------------ onboarding
def onboarding():
    ss = st.session_state
    md('<div class="nk-hero"><div class="nk-mascot">🐿️</div><div class="nk-title">' + esc(T("Hi, I am Chintu!")) + '</div>'
       '<small>' + T("Welcome to <b>EasyFin</b>. Learn how money works through stories, games and quizzes. Ages 5 to 14.") + '</small><br><small style="opacity:.85">powered by NYZTrade</small></div>')
    names = storage.profile_names()
    if names:
        md(f'<div class="nk-title" style="font-size:1.05rem">{esc(T("Welcome back"))}</div>')
        for n in names[:8]:
            st.button(f"🐿️ {n}", key=f"prof-{n}", on_click=open_profile, args=(n,))
        md(f'<div class="nk-sub" style="text-align:center">{esc(T("or start a new learner"))}</div>')
    with st.container(key="card-new"):
        st.text_input(T("Pick a nickname (not your full name)"), key="nick", max_chars=20, placeholder=T("e.g. Aarav"))
        md(f'<div class="nk-sub">{esc(T("Choose your age group"))}</div>')
        band_buttons(ss.pick_band, pick_onboard_band, "ob")
        st.checkbox(T("My parent or guardian is with me and agrees"), key="consent")
        if ss.err:
            ui.md(f'<div class="nk-fb no">{esc(T(ss.err))}</div>')
        st.button(T("Let us start ➜"), key="start", type="primary", on_click=start_profile)
    footer()


# ------------------------------------------------------------------ learn
def learn():
    ss = st.session_state
    P = ss.P
    lv, into = level(P["xp"])
    done_n = len(P["done"])
    md(f'<div class="nk-hero"><div class="nk-mascot">🐿️</div><div class="nk-title">{esc(T("Hi {name}!", name=ss.name))}</div>'
       f'<small>{esc(T("{done} of {total} lessons done. Keep going!", done=done_n, total=len(C.LESSONS)))}</small>'
       f'<div style="margin-top:10px;background:rgba(255,255,255,.28);border-radius:99px;height:12px;overflow:hidden"><i style="display:block;height:100%;width:{into}%;background:#FFD27A;border-radius:99px"></i></div>'
       f'<small>{esc(T("Level {lv}, {xp} XP to level {next}", lv=lv, xp=100 - into, next=lv + 1))}</small></div>')
    stats_row(P)
    band_buttons(P["band"], set_band, "lb")
    band = i18n.band(P["band"])
    md(f'<div class="nk-sub" style="text-align:center">{esc(band["note"])}</div>')
    for l in i18n.lessons_for(P["band"]):
        s = P["done"].get(l["id"], 0)
        with st.container(key=f"card-{l['id']}"):
            md(f'<div class="nk-row"><div class="nk-art">{l["art"]}</div><div class="nk-grow"><div class="nk-title" style="font-size:1.1rem">{esc(l["title"])}</div>'
               f'<div class="nk-sub">{esc(l["blurb"])}</div></div></div>'
               f'<div class="nk-stars" style="color:var(--sun);margin:6px 0 2px">{ui.stars(s)}</div>')
            st.button(T("Play again") if s else T("Play ➜"), key=f"play-{l['id']}", type="secondary" if s else "primary",
                      on_click=open_lesson, args=(l["id"],))


# ------------------------------------------------------------------ lesson
def exit_lesson():
    go("learn")


def lesson_view():
    ss = st.session_state
    l = i18n.lesson(ss.lesson)
    with st.container(key="ns-lhead"):
        c1, c2 = st.columns([1, 3])
        with c1:
            st.button("✕", key="exit", on_click=exit_lesson)
        with c2:
            md(f'<div class="nk-title" style="padding-top:6px">{l["art"]} {esc(l["title"])}</div>')
    if ss.stage == "story":
        story_view(l)
    elif ss.stage == "game":
        game_view(l)
    else:
        quiz_view(l)


def story_view(l):
    ss = st.session_state
    n = len(l["story"])
    em, text = l["story"][ss.step]
    md(ui.dots(ss.step, ss.step, n))
    md(f'<div class="nk-story nk-pop"><div class="em">{em}</div><p>{esc(text)}</p></div>')
    if ss.listen:
        voice.listen(text)
    with st.container(key="ns-story-nav"):
        c1, c2 = st.columns([1, 2])
        with c1:
            st.button(T("◀ Back"), key="story-back", on_click=story_move, args=(-1, n), disabled=ss.step == 0)
        with c2:
            st.button(T("Next ▶") if ss.step < n - 1 else T("Let us play! 🎮"), key="story-next", type="primary", on_click=story_move, args=(1, n))


def game_view(l):
    ss = st.session_state
    finished = activities.play(l)
    if finished:
        st.button(T("Take the quiz ➜"), key="to-quiz", type="primary", on_click=to_quiz, args=(l["id"],))


def quiz_view(l=None):
    ss = st.session_state
    qz = ss.quiz
    if qz is None:
        to_quiz(l["id"])
        qz = ss.quiz
    if qz["result"]:
        return result_view(l)
    n = len(qz["qs"])
    q = qz["qs"][qz["i"]]
    q_text, raw_opts, _ans, why = i18n.question(q["lid"], q["idx"])
    opts = [raw_opts[j] for j in q["order"]]
    md(ui.dots(qz["i"], qz["i"], n))
    md(f'<div class="nk-sub" style="text-align:center">{esc(T("Question {i} of {n}", i=qz["i"] + 1, n=n))}</div>')
    md(f'<div class="nk-q">{esc(q_text)}</div>')
    if ss.listen:
        voice.listen(q_text)   # question only, so one saved clip serves every shuffled order
    for oi, text in enumerate(opts):
        if qz["answered"]:
            state = "ok" if oi == q["right"] else "opt"
        else:
            state = "no" if oi in qz["wrong"] else "opt"
        with st.container(key=f"{state}-q{qz['i']}-{oi}"):
            st.button(text, key=f"q{qz['i']}-o{oi}", on_click=pick, args=(oi,), disabled=qz["answered"] or oi in qz["wrong"])
    if qz["answered"]:
        first = not qz["wrong"]
        ui.md(f'<div class="nk-fb ok nk-pop">{esc(T("Great job!") if first else T("You got it!"))} {esc(why)}</div>')
        last = qz["i"] + 1 >= n
        st.button(T("See my results ➜") if last else T("Next question ➜"), key="next-q", type="primary", on_click=next_q)
    elif qz["wrong"]:
        ui.md(f'<div class="nk-fb hint">{esc(T("Not quite. That is okay. Try another answer."))}</div>')


def result_view(l):
    ss = st.session_state
    qz = ss.quiz
    res = qz["result"]
    n = len(qz["qs"])
    if qz["kind"] == "lesson":
        md(f'<div class="nk-hero nk-pop" style="text-align:center"><div class="nk-title">{esc(T("Lesson complete!"))}</div>'
           f'<div style="font-size:2.6rem;letter-spacing:6px;margin:6px 0">{"⭐" * res["stars"]}{"☆" * (3 - res["stars"])}</div>'
           f'<small>{esc(T("{ok} of {n} right on the first try. +{xp} XP", ok=qz["first_ok"], n=n, xp=qz["xp"]))}</small></div>')
        md(f'<div class="nk-card"><div class="nk-title" style="font-size:1.05rem">{esc(T("Talk about it at home"))}</div><div class="nk-sub">{esc(l["talk"])}</div></div>')
    else:
        md(f'<div class="nk-hero nk-pop" style="text-align:center"><div class="nk-title">{esc(T("Quick Quiz done!"))}</div>'
           f'<div class="nk-big" style="color:#fff">{qz["first_ok"]} / {n}</div><small>+{qz["xp"]} XP</small></div>')
    for bid in res["new"]:
        name, em, desc = badge_info(bid)
        md(f'<div class="nk-fb hint nk-pop">{em} {T("New badge: <b>{name}</b>.", name=esc(name))} {esc(desc)}</div>')
    if qz["kind"] == "lesson":
        with st.container(key="ns-res-act"):
            c1, c2 = st.columns(2)
            with c1:
                st.button(T("Play again"), key="res-again", on_click=open_lesson, args=(l["id"],))
            with c2:
                st.button(T("Back to lessons"), key="res-back", type="primary", on_click=go, args=("learn",))
    else:
        with st.container(key="ns-res-act"):
            c1, c2 = st.columns(2)
            with c1:
                st.button(T("Another round"), key="res-again", on_click=start_quick)
            with c2:
                st.button(T("Back to lessons"), key="res-back", type="primary", on_click=go, args=("learn",))


# ------------------------------------------------------------------ quick quiz
def quick_view():
    ss = st.session_state
    P = ss.P
    if ss.quiz and ss.quiz["kind"] == "quick":
        return quiz_view(None)
    md('<div class="nk-hero"><div class="nk-mascot">⚡</div><div class="nk-title">' + esc(T("Quick Quiz")) + '</div>'
       '<small>' + esc(T("10 mixed questions from the whole age group. Earn XP and try for 10 out of 10!")) + '</small></div>')
    band_buttons(ss.quick_band, pick_quick_band, "qb")
    pool = len(band_refs(ss.quick_band))
    best = P["quick_best"].get(ss.quick_band)
    best_txt = f"{best} / 10" if best is not None else T("none yet")
    md(f'<div class="nk-card"><div class="nk-sub">{T("{pool} questions in this group. Best score: <b>{best}</b>", pool=pool, best=esc(best_txt))}</div></div>')
    st.button(T("Start 10 questions ➜"), key="quick-start", type="primary", on_click=start_quick)


# ------------------------------------------------------------------ rewards
def rewards_view():
    ss = st.session_state
    P = ss.P
    lv, into = level(P["xp"])
    md(f'<div class="nk-hero"><div class="nk-mascot">🏆</div><div class="nk-title">{esc(T("Level {lv}", lv=lv))}</div>'
       f'<small>{esc(T("{xp} XP in total. {left} XP to the next level.", xp=P["xp"], left=100 - into))}</small>'
       f'<div style="margin-top:10px;background:rgba(255,255,255,.28);border-radius:99px;height:12px;overflow:hidden"><i style="display:block;height:100%;width:{into}%;background:#FFD27A;border-radius:99px"></i></div></div>')
    stats_row(P)
    md(f'<div class="nk-title" style="margin-top:6px">{esc(T("Lesson badges"))}</div>')
    cells = ""
    for l in i18n.all_lessons():
        got = "L:" + l["id"] in P["badges"]
        cells += f'<div class="nk-badge {"" if got else "locked"}"><div class="em">{l["badge"][1]}</div><b>{esc(l["badge"][0])}</b><span>{ui.stars(P["done"].get(l["id"], 0))}</span></div>'
    md(f'<div class="nk-grid">{cells}</div>')
    md(f'<div class="nk-title" style="margin-top:6px">{esc(T("Special badges"))}</div>')
    cells = ""
    for gid, name, em, desc in GLOBAL_BADGES:
        got = gid in P["badges"]
        cells += f'<div class="nk-badge {"" if got else "locked"}"><div class="em">{em}</div><b>{esc(T(name))}</b><span>{esc(T(desc))}</span></div>'
    md(f'<div class="nk-grid">{cells}</div>')


# ------------------------------------------------------------------ parent
def parent_view():
    ss = st.session_state
    P = ss.P
    if not ss.parent_ok:
        if "gate_answer" not in ss:
            a, b = random.randint(6, 9), random.randint(6, 9)
            ss.gate_q, ss.gate_answer = f"{a} × {b}", a * b
        md('<div class="nk-hero"><div class="nk-mascot">👪</div><div class="nk-title">' + esc(T("Parent corner")) + '</div><small>' + esc(T("A quick grown-up check, then you can see progress and settings.")) + '</small></div>')
        with st.container(key="card-gate"):
            st.text_input(T("What is {q}?", q=ss.gate_q), key="gate", max_chars=3)
            if ss.err:
                ui.md(f'<div class="nk-fb no">{esc(T(ss.err))}</div>')
            st.button(T("Open"), key="gate-open", type="primary", on_click=check_gate)
        return
    acc = round(P["q_first"] / P["q_total"] * 100) if P["q_total"] else 0
    minutes = round(P["seconds"] / 60)
    progress_title = T("{name}'s progress", name=esc(ss.name))
    md(f'<div class="nk-hero"><div class="nk-mascot">👪</div><div class="nk-title">{progress_title}</div>'
       f'<small>{esc(T("Age group: {band} · learning since {date}", band=i18n.band(P["band"])["name"], date=P["created"]))}</small></div>')
    md(f'<div class="nk-stats"><div class="nk-stat"><b>{len(P["done"])}/{len(C.LESSONS)}</b><span>{esc(T("lessons"))}</span></div>'
       f'<div class="nk-stat"><b>{acc}%</b><span>{esc(T("first-try right"))}</span></div>'
       f'<div class="nk-stat"><b>{minutes}</b><span>{esc(T("minutes"))}</span></div>'
       f'<div class="nk-stat"><b>{P["streak"]}</b><span>{esc(T("day streak"))}</span></div></div>')
    for b in i18n.bands():
        ls = C.lessons_for(b["id"])
        d = sum(1 for l in ls if l["id"] in P["done"])
        md(f'<div class="nk-card"><div class="nk-row"><div class="nk-grow"><div class="nk-title" style="font-size:1rem">{esc(b["name"])} · {esc(b["ages"])}</div>'
           f'<div class="nk-sub">{esc(T("{d} of {n} lessons", d=d, n=len(ls)))}</div></div></div><div style="margin-top:6px">{ui.bar(d / len(ls) * 100, True)}</div></div>')
    md(f'<div class="nk-title" style="margin-top:6px">{esc(T("Talk at home"))}</div>')
    rows = ""
    for l in i18n.all_lessons():
        s = P["done"].get(l["id"], 0)
        mark = ui.stars(s) if s else T("not yet")
        rows += f'<tr><td>{l["art"]} <b>{esc(l["title"])}</b><br><span class="nk-sub">{esc(l["talk"])}</span></td><td style="white-space:nowrap">{mark}</td></tr>'
    md(f'<div class="nk-card"><table class="nk-table"><tr><th>{esc(T("Lesson and conversation starter"))}</th><th>{esc(T("Stars"))}</th></tr>{rows}</table></div>')
    md(f'<div class="nk-card"><div class="nk-title" style="font-size:1rem">{esc(T("Question bank"))}</div><div class="nk-sub">{esc(T("{q} questions across {l} lessons. Each play draws {k} at random, so replays feel fresh.", q=C.total_questions(), l=len(C.LESSONS), k=C.QUESTIONS_PER_PLAY))}</div></div>')
    md(f'<div class="nk-title" style="margin-top:6px">{esc(T("Settings"))}</div>')
    with st.container(key="ns-set"):
        c1, c2 = st.columns(2)
        with c1:
            st.button(T(THEME_LABEL[ss.theme]), key="set-theme", on_click=cycle_theme)
        with c2:
            st.button(T("🔊 Read aloud: on") if ss.listen else T("🔊 Read aloud: off"), key="set-listen", on_click=toggle_listen)
    st.download_button(T("Download progress (JSON)"), storage.export_json(ss.name), file_name=f"easyfin-{ss.name}.json", mime="application/json")
    with st.container(key="ns-set2"):
        c1, c2 = st.columns(2)
        with c1:
            st.button(T("Switch learner"), key="set-switch", on_click=switch_child)
        with c2:
            st.button(T("🔒 Lock"), key="set-lock", on_click=lock_parent)
    if not ss.confirm_reset:
        st.button(T("Delete this learner's data"), key="reset", on_click=ask_reset)
    else:
        ui.md(f'<div class="nk-fb no">{esc(T("This deletes all progress for this learner. It cannot be undone."))}</div>')
        with st.container(key="ns-reset"):
            c1, c2 = st.columns(2)
            with c1:
                st.button(T("Yes, delete"), key="reset-yes", on_click=do_reset)
            with c2:
                st.button(T("Keep it"), key="reset-no", on_click=cancel_reset)
    md(f'<div class="nk-card"><div class="nk-title" style="font-size:1rem">{esc(T("Voice"))}</div>'
       f'<div class="nk-sub">{esc(voice.status())}</div></div>')
    voice.listen("നമസ്കാരം, ഞാൻ ചിന്റു ആണ്. നമുക്ക് പണത്തെക്കുറിച്ച് പഠിക്കാം.", force="ml")
    md(f'<div class="nk-card"><div class="nk-title" style="font-size:1rem">{esc(T("Privacy and safety"))}</div>'
       f'<div class="nk-sub">{esc(T("Only a nickname and progress are stored, on this device. No ads, no chat, no real money. If you run this online for children, get verifiable parental consent as required by the DPDP Act and Rules, and keep the content educational only."))}</div></div>')


# ------------------------------------------------------------------ main
def main():
    init()
    ss = st.session_state
    ui.inject(ss.theme, ss.lang)
    if ss.P is None:
        topbar()
        onboarding()
        return
    tick()
    if ss.lesson:
        lesson_view()
        footer()
        return
    topbar()
    nav()
    {"learn": learn, "quick": quick_view, "rewards": rewards_view, "parent": parent_view}[ss.page]()
    footer()


main()
