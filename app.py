"""EasyFin, powered by NYZTrade. SINGLE FILE VERSION.

Everything (content, storage, styling, games and screens) is in this one file, so it
deploys by uploading only app.py plus requirements.txt. The first part below holds the
supporting modules as text. The app itself starts after the line  # ===== APP =====
"""
import os as _os
import sys as _sys
import types as _types

_SOURCES = {}
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


# ----------------------------------------------------------------- Self checks
assert len(LESSONS) == 22
for _l in LESSONS:
    assert len(_l["story"]) == 3, _l["id"]
    assert len(_l["bank"]) == 12, (_l["id"], len(_l["bank"]))
    for _q in _l["bank"]:
        assert len(_q) == 4 and 0 <= _q[2] < len(_q[1]) and len(_q[1]) >= 3, (_l["id"], _q[0])
    if _l["act"]["type"] == "sort":
        for _i in _l["act"]["items"]:
            assert 0 <= _i[2] < len(_l["act"]["labels"]), (_l["id"], _i)
assert total_questions() == 264
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
DEFAULT_SETTINGS = {"theme": "auto", "listen": True, "last_profile": ""}


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
_SOURCES['ui'] = r'''"""Look and feel: light, dark and auto themes, plus small HTML helpers."""
import html
import json

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
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Lexend:wght@400;500;600&display=swap');
html,body,.stApp,[data-testid="stAppViewContainer"]{background:var(--bg)!important;color:var(--ink)}
.stApp{font-family:'Lexend',system-ui,sans-serif}
[data-testid="stHeader"]{background:transparent!important;height:0}
[data-testid="stToolbar"],[data-testid="stDecoration"],footer,#MainMenu{display:none!important}
.block-container{max-width:760px!important;padding:1rem 16px 5rem!important}
.stApp p,.stApp li,.stApp label,.stApp span,.stApp div[data-testid="stMarkdownContainer"]{color:inherit}
h1,h2,h3,.nk-title{font-family:'Baloo 2','Lexend',sans-serif!important;color:var(--ink)!important;letter-spacing:0}
[data-testid="stVerticalBlock"]{gap:.7rem}

/* keep rows side by side on phones */
[class*="st-key-ns-"] [data-testid="stHorizontalBlock"]{flex-direction:row!important;flex-wrap:nowrap!important;gap:.5rem!important}
[class*="st-key-ns-"] [data-testid="stColumn"],[class*="st-key-ns-"] [data-testid="column"]{min-width:0!important}

/* buttons */
.stButton,[data-testid="stElementContainer"]:has(>.stButton),[data-testid="stButton"]{width:100%!important}
.stButton>button,[data-testid="stButton"]>button{width:100%!important;min-height:3rem;border-radius:16px;border:2px solid var(--line);background:var(--card);color:var(--ink);
  font-family:'Lexend',sans-serif;font-weight:600;box-shadow:0 3px 0 var(--line);transition:transform .08s,border-color .15s;padding:.4rem .8rem}
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
.nk-stat b{display:block;font-family:'Baloo 2',sans-serif;font-size:1.35rem;line-height:1.1}
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
.nk-big{font-family:'Baloo 2',sans-serif;font-size:2.4rem;font-weight:800;text-align:center;line-height:1.1}
.nk-big small{display:block;font-size:.8rem;color:var(--muted);font-weight:500;font-family:'Lexend',sans-serif}
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


def inject(mode):
    st.markdown(f"<style>{theme_css(mode)}{BASE_CSS}</style>", unsafe_allow_html=True)


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


LISTEN_HTML = """
<style>
html,body{margin:0;background:transparent;font-family:system-ui,sans-serif}
button{display:inline-flex;gap:8px;align-items:center;min-height:40px;padding:0 16px;border-radius:99px;background:#F5A524;color:#3B2800;font-weight:700;font-size:14px;border:0;cursor:pointer;font-family:inherit}
button:focus-visible{outline:3px solid #0B7A75;outline-offset:2px}
#n{font-size:12px;color:#7a8b87;margin-top:4px}
</style>
<button id="b" type="button">🔊 Listen</button><div id="n" hidden></div>
<script>
const T=__TEXT__;
document.getElementById('b').addEventListener('click',function(){
  const n=document.getElementById('n');
  try{
    const s=window.speechSynthesis;
    if(!s||!window.SpeechSynthesisUtterance){n.textContent='This browser cannot read aloud.';n.hidden=false;return}
    s.cancel();const u=new SpeechSynthesisUtterance(T);u.lang='en-IN';u.rate=.9;
    const v=(s.getVoices()||[]).find(function(x){return x.lang.replace('_','-').toLowerCase()==='en-in'});if(v)u.voice=v;s.speak(u);
  }catch(e){}
});
</script>
"""


def listen(text):
    page = LISTEN_HTML.replace("__TEXT__", json.dumps(text))
    if hasattr(st, "iframe"):
        st.iframe(page.strip(), height=52)
    else:  # Streamlit 1.41 to 1.5x
        import streamlit.components.v1 as components
        components.html(page, height=52)
'''
_SOURCES['activities'] = r'''"""Mini games. Every game has the signature game(lesson) -> bool (finished?).

State lives in st.session_state["act"], which the app resets for each lesson.
All money is practice money. Rates and prices are examples, not predictions.
"""
import random

import streamlit as st

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


def feedback(kind, text):
    md(f'<div class="nk-fb {kind}">{esc(text)}</div>')


def progress_hint(need, have, what):
    md(f'<div class="nk-sub" style="text-align:center">{what}: {min(have, need)} of {need}</div>')


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
            a["msg"] = ("ok", "Perfect! You paid exactly the right amount.")
        else:
            a["r"] += 1
            a["coins"] = []
            a["msg"] = ("ok", "Yes! Exactly right. Here comes the next one.")
    elif total < target:
        a["msg"] = ("hint", f"Not enough yet. You need {inr(target - total)} more.")
    else:
        a["msg"] = ("no", f"That is {inr(total - target)} too much. Press Undo and try again.")


def coins(lesson):
    a = A()
    rounds = lesson["act"]["rounds"]
    a.setdefault("r", 0)
    a.setdefault("coins", [])
    a.setdefault("msg", None)
    rd = rounds[min(a["r"], len(rounds) - 1)]
    total = sum(a["coins"])
    chips_html = "".join(f"<span>{inr(c)}</span>" for c in a["coins"]) or '<span style="opacity:.5">Tap coins and notes</span>'
    md(f'<div class="nk-card"><div class="nk-big">{rd["item"]}<small>{esc(rd["say"])}</small>{inr(rd["target"])}</div></div>')
    md(f'<div class="nk-card"><div class="nk-money">{chips_html}</div><div class="nk-big" style="margin-top:6px">{inr(total)}<small>you have paid</small></div></div>')
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
                st.button("↩ Undo", key="coin-undo", on_click=_coin_undo)
            with c2:
                st.button("Clear", key="coin-clear", on_click=_coin_clear)
            with c3:
                st.button("Check ✓", key="coin-check", type="primary", on_click=_coin_check, args=(rounds,))
    if a["msg"]:
        feedback(*a["msg"])
    return bool(a.get("done"))


# ----------------------------------------------------------------- sort
def _sort_pick(items, idx):
    a = A()
    item = items[a["i"]]
    if idx == item[2]:
        a["msg"] = ("ok", item[3])
        a["i"] += 1
        a["lastok"] = True
        if a["i"] >= len(items):
            a["done"] = True
    else:
        a["wrong"] += 1
        a["msg"] = ("hint", "Not quite. Think again. " + item[3])


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
           f'<div class="nk-sub">Item {a["i"] + 1} of {len(items)}. Where does it belong?</div></div>')
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
        feedback(*a["msg"])
    if a.get("done"):
        md(f'<div class="nk-fb ok nk-pop">All sorted! You made {a["wrong"]} slip{"s" if a["wrong"] != 1 else ""}.</div>')
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
    md(f'<div class="nk-card"><div class="nk-big">{cfg["item"]} 🐷<small>Goal: a {esc(cfg["what"])} for {inr(cfg["goal"])}</small>'
       f'{inr(a["amount"])}</div><div style="margin-top:10px">{bar(pct)}</div>'
       f'<div class="nk-sub" style="text-align:center;margin-top:6px">{esc(cfg["unit"])} {a["n"]}</div></div>')
    if not a.get("done"):
        st.button(f'Save {inr(cfg["step"])} this {cfg["unit"].lower()} 🪙', key="piggy-save", type="primary",
                  on_click=_piggy_save, args=(cfg["step"], cfg["goal"]))
        st.caption("Small, regular steps reach the goal.")
    else:
        feedback("ok", f'You reached {inr(cfg["goal"])} in {a["n"]} {cfg["unit"].lower()}s by saving {inr(cfg["step"])} each time. Patience paid off!')
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
        a["msg"] = ("hint", f"You still have {inr(left)} to place. Every rupee needs a job.")
        return
    if cfg["kind"] == "jars":
        if any(x == 0 for x in v.values()):
            a["msg"] = ("hint", "Give every jar at least a little. Even Share and Save matter.")
        elif v["save"] < total * 0.2:
            a["msg"] = ("hint", "Try to save at least a fifth of your money. Future you will say thanks!")
        else:
            a["done"] = True
            a["msg"] = ("ok", "Nice split. Every jar has a job and your savings are growing.")
    else:
        if v["school"] < total * 0.25:
            a["msg"] = ("hint", "Needs come first. Give School things at least a quarter of your money.")
        elif v["save"] < total * 0.1:
            a["msg"] = ("hint", "Add at least a tenth to Savings, so you can handle surprises.")
        elif v["snacks"] + v["fun"] > total * 0.5:
            a["msg"] = ("hint", "Snacks and Fun together are more than half. Can you trim a little?")
        else:
            a["done"] = True
            a["msg"] = ("ok", "A balanced budget! Needs first, then savings, then fun.")


def alloc(lesson):
    a = A()
    cfg = lesson["act"]
    total, step = cfg["total"], cfg["step"]
    a.setdefault("vals", {k: 0 for k, _ in cfg["cats"]})
    a.setdefault("msg", None)
    left = total - sum(a["vals"].values())
    md(f'<div class="nk-card"><div class="nk-big">{inr(left)}<small>left to place out of {inr(total)}</small></div></div>')
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
        st.button("Check my plan ✓", key="alloc-check", type="primary", on_click=_alloc_check, args=(cfg,))
    if a["msg"]:
        feedback(*a["msg"])
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
    md(f'<div class="nk-card" style="text-align:center"><div class="nk-big">{emoji}<small>{esc(name)} at the {esc(cfg["product"])} stall. Each {esc(cfg["unit"])} costs {inr(cfg["cost"])} to make.</small></div>'
       f'<div class="nk-sub" style="margin-top:6px">Goal today: a profit of at least <b>{inr(goal)}</b> (try {a["runs"] + 0} of 4)</div></div>')
    md(f'<div class="nk-card"><div class="nk-big">{inr(a["price"])}<small>price per {esc(cfg["unit"])}</small></div></div>')
    s1, s2 = cfg["steps"]
    with st.container(key="ns-stall-price"):
        cols = st.columns(4)
        for col, d in zip(cols, [-s2, -s1, s1, s2]):
            with col:
                st.button(("+" if d > 0 else "−") + str(abs(d)), key=f"stall-p{d}", on_click=_stall_price,
                          args=(d, cfg["pmin"], cfg["pmax"]), disabled=bool(a.get("done")))
    res = a["result"]
    if not a.get("done"):
        st.button(f'Open the stall ({emoji})', key="stall-run", type="primary", on_click=_stall_run, args=(cfg,))
    if res:
        md(f'<div class="nk-card"><table class="nk-table"><tr><th>Sold</th><th>Money in</th><th>Costs</th><th>Profit</th></tr>'
           f'<tr><td>{res["sold"]}</td><td>{inr(res["income"])}</td><td>{inr(res["costs"])}</td><td><b>{inr(res["profit"])}</b></td></tr></table></div>')
        if res["profit"] >= res["goal"]:
            feedback("ok", "Goal reached! Profit is what is left after costs, and you found a price customers like.")
        elif res["profit"] < 0:
            feedback("no", "A loss. You paid more to make the goods than you earned. Raise the price a little.")
        elif res["sold"] == 0:
            feedback("hint", "Nobody bought anything. That price is too high. Try lowering it.")
        elif res["lo"] is not None:
            feedback("hint", f"Close. On a day like this, prices between {inr(res['lo'])} and {inr(res['hi'])} reach the goal.")
        else:
            feedback("hint", "This is a tough day. Do your best price, then try another day.")
        if a.get("done") and not a.get("won"):
            feedback("hint", "That is 4 tries. Real shopkeepers keep adjusting too. Let us move on to the quiz.")
    if res and not a.get("done"):
        st.button("Try another day ➜", key="stall-next", on_click=_stall_new_day, args=(days,))
    return bool(a.get("done"))


# ----------------------------------------------------------------- order
def _order_pick(step_text, steps):
    a = A()
    if step_text == steps[len(a["placed"])]:
        a["placed"].append(step_text)
        a["msg"] = ("ok", "Yes!")
        if len(a["placed"]) == len(steps):
            a["done"] = True
            a["msg"] = ("ok", "All in the right order. Safe paying habit unlocked!")
    else:
        a["wrong"] += 1
        a["msg"] = ("hint", "Not that one yet. What happens first, before money moves?")


def order(lesson):
    a = A()
    cfg = lesson["act"]
    steps = cfg["steps"]
    if "shuffled" not in a:
        s = steps[:]
        for _ in range(10):
            random.shuffle(s)
            if s != steps:
                break
        a["shuffled"], a["placed"], a["wrong"], a["msg"] = s, [], 0, None
    md(f'<div class="nk-title" style="text-align:center">{esc(cfg["title"])}</div>')
    placed = "".join(f'<tr><td><b>{i + 1}</b></td><td>{esc(t)}</td></tr>' for i, t in enumerate(a["placed"])) or '<tr><td colspan="2" class="nk-sub">Tap the steps below in order</td></tr>'
    md(f'<div class="nk-card"><table class="nk-table">{placed}</table></div>')
    if not a.get("done"):
        for t in [x for x in a["shuffled"] if x not in a["placed"]]:
            st.button(t, key=f"ord-{t}", on_click=_order_pick, args=(t, steps))
    if a["msg"]:
        feedback(*a["msg"])
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
    md('<div class="nk-sub">Monthly saving</div>')
    chips("gm", [500, 1000, 2000, 5000], a["monthly"], inr, "monthly")
    md('<div class="nk-sub">Example yearly growth (not a promise)</div>')
    chips("gr", [6, 8, 12], a["rate"], lambda x: f"{x}%", "rate")
    md('<div class="nk-sub">Years</div>')
    chips("gy", [5, 10, 15, 20, 30], a["years"], lambda x: f"{x}y", "years", seen_key=["years"])
    put = a["monthly"] * 12 * a["years"]
    val = fv(a["monthly"], a["rate"], a["years"])
    later = fv(a["monthly"], a["rate"], max(0, a["years"] - 5))
    md(f'<div class="nk-card"><div class="nk-big">{inr(val)}<small>after {a["years"]} years</small></div>'
       f'<div class="nk-sub" style="margin-top:8px">You put in {inr(put)}</div>{bar(put / val * 100, True)}'
       f'<div class="nk-sub" style="margin-top:6px">Growth on growth: {inr(val - put)}</div>{bar((val - put) / val * 100)}</div>')
    if a["years"] > 5:
        md(f'<div class="nk-fb hint">Start 5 years later and the same saving grows to only {inr(later)}. Starting early is a superpower.</div>')
    seen = len(set(a["seen"]))
    if seen >= 3:
        a["done"] = True
    else:
        progress_hint(3, seen, "Try different years. Years tried")
    md('<div class="nk-sub" style="text-align:center">Example only. Real returns go up and down and are never guaranteed.</div>')
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
    md(f'<div class="nk-card"><div class="nk-big">{inr(left)}<small>practice money left to place (made-up companies)</small></div></div>')
    for key, em, name, note in COMPANIES:
        with st.container(key=f"card-mk-{key}"):
            with st.container(key=f"ns-mk-{key}"):
                c1, c2, c3 = st.columns([3, 1, 1])
                with c1:
                    md(f'<div class="nk-title" style="font-size:1rem">{em} {esc(name)}</div><div class="nk-sub">{esc(note)} · {inr(a["vals"][key])}</div>')
                with c2:
                    st.button("−", key=f"mk-m-{key}", on_click=_mkt_move, args=(key, -1))
                with c3:
                    st.button("+", key=f"mk-p-{key}", on_click=_mkt_move, args=(key, 1))
    ready = left == 0
    if not ready:
        md('<div class="nk-sub" style="text-align:center">Place all your practice money to start the years.</div>')
    with st.container(key="ns-mk-years"):
        cols = st.columns(len(YEARS))
        for i, col in enumerate(cols):
            with col:
                st.button(YEARS[i][0], key=f"mk-y{i}", on_click=_mkt_run, args=(i,), disabled=not ready)
    if a["last"]:
        name, rets, value = a["last"]
        change = value - MARKET_TOTAL
        rows = "".join(f'<tr><td>{em} {esc(nm)}</td><td>{rets[k]:+d}%</td></tr>' for k, em, nm, _ in COMPANIES)
        kind = "ok" if change >= 0 else "no"
        md(f'<div class="nk-card"><div class="nk-title">{esc(name)}</div><table class="nk-table"><tr><th>Company</th><th>Year result</th></tr>{rows}</table></div>')
        feedback(kind, f"Your practice money is now {inr(value)} ({'+' if change >= 0 else '−'}{inr(abs(change))}).")
    if a.get("done"):
        spread = sum(1 for v in a["vals"].values() if v > 0)
        if spread >= 3:
            feedback("hint", "You spread your money across several companies, so no single bad year hurt too much. That is diversification.")
        else:
            feedback("hint", "Your money sat in few companies, so results swung more. Spreading across more companies usually smooths the ride.")
    else:
        progress_hint(len(YEARS), len(a["ran"]), "Years played")
    md('<div class="nk-sub" style="text-align:center">Made-up companies and made-up years. This is a learning game, never advice to buy anything.</div>')
    return bool(a.get("done"))


# ----------------------------------------------------------------- inflation
def inflation(lesson):
    a = A()
    a.setdefault("years", 10)
    a.setdefault("rate", 6)
    a.setdefault("seen", ["10|6"])
    md('<div class="nk-sub">Years from now</div>')
    chips("iy", [5, 10, 20, 30], a["years"], lambda x: f"{x}y", "years", seen_key=["years", "rate"])
    md('<div class="nk-sub">Example yearly price rise</div>')
    chips("ir", [4, 6, 8], a["rate"], lambda x: f"{x}%", "rate", seen_key=["years", "rate"])
    cost = 100 * (1 + a["rate"] / 100) ** a["years"]
    buys = 100 / (1 + a["rate"] / 100) ** a["years"]
    md(f'<div class="nk-card"><div class="nk-big">🍿 {inr(cost)}<small>what a ₹100 snack costs in {a["years"]} years</small></div>'
       f'<div class="nk-sub" style="margin-top:8px">₹100 kept idle will then buy only this much of today\'s snack:</div>{bar(buys)}'
       f'<div class="nk-sub" style="margin-top:4px"><b>{buys:.0f}%</b> of it</div></div>')
    seen = len(set(a["seen"]))
    if seen >= 3:
        a["done"] = True
    else:
        progress_hint(3, seen, "Try other settings. Combinations tried")
    md('<div class="nk-sub" style="text-align:center">Example rates for learning. Real inflation changes from year to year.</div>')
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
    md('<div class="nk-sub">Amount borrowed</div>')
    chips("lp", [20000, 50000, 100000], a["principal"], inr, "principal", seen_key=keys)
    md('<div class="nk-sub">Example yearly interest rate</div>')
    chips("lr", [8, 12, 24], a["rate"], lambda x: f"{x}%", "rate", seen_key=keys)
    md('<div class="nk-sub">Years to repay</div>')
    chips("ly", [1, 2, 3, 5], a["years"], lambda x: f"{x}y", "years", seen_key=keys)
    m = emi(a["principal"], a["rate"], a["years"])
    total = m * a["years"] * 12
    extra = total - a["principal"]
    md(f'<div class="nk-card"><div class="nk-big">{inr(m)}<small>EMI, paid every month</small></div>'
       f'<table class="nk-table" style="margin-top:8px"><tr><td>You borrow</td><td><b>{inr(a["principal"])}</b></td></tr>'
       f'<tr><td>You pay back</td><td><b>{inr(total)}</b></td></tr>'
       f'<tr><td>Extra cost (interest)</td><td><b>{inr(extra)}</b></td></tr></table>'
       f'<div style="margin-top:8px">{bar(extra / total * 100)}</div><div class="nk-sub">{extra / total * 100:.0f}% of what you pay is interest</div></div>')
    seen = len(set(a["seen"]))
    if seen >= 3:
        a["done"] = True
    else:
        progress_hint(3, seen, "Try other settings. Combinations tried")
    md('<div class="nk-sub" style="text-align:center">Example only. Borrow from trusted, regulated lenders and ask a grown-up first.</div>')
    return bool(a.get("done"))


ENGINES = {
    "coins": coins, "sort": sort, "piggy": piggy, "alloc": alloc, "stall": stall, "order": order,
    "grow": grow, "market": market, "inflation": inflation, "loan": loan,
}


def play(lesson):
    return ENGINES[lesson["act"]["type"]](lesson)
'''

_HERE = _os.path.dirname(_os.path.abspath(__file__))
for _name in ("content", "storage", "ui", "activities"):
    if _name not in _sys.modules:
        _mod = _types.ModuleType(_name)
        _mod.__file__ = _os.path.join(_HERE, _name + ".py")
        _sys.modules[_name] = _mod
        exec(compile(_SOURCES[_name], _mod.__file__, "exec"), _mod.__dict__)

# ===== APP =====
"""EasyFin, powered by NYZTrade: money learning for ages 5 to 14.  Run:  streamlit run app.py

Practice money only. No real trading, no tips, no advice.
"""
import datetime
import random
import time

import streamlit as st

import activities
import content as C
import storage
import ui
from ui import esc, inr, md

st.set_page_config(page_title="EasyFin | powered by NYZTrade", page_icon="🐿️", layout="centered", initial_sidebar_state="collapsed")

THEMES = ["auto", "light", "dark"]
THEME_LABEL = {"auto": "🌓 Auto", "light": "☀️ Light", "dark": "🌙 Dark"}

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
    if "boot" in ss:
        return
    ss.boot = True
    s = storage.settings()
    ss.theme = s["theme"] if s["theme"] in THEMES else "auto"
    ss.listen = bool(s["listen"])
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
    storage.save_settings({"theme": ss.theme, "listen": ss.listen, "last_profile": ss.name or ""})


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
        l = C.LESSON_BY_ID[bid[2:]]
        return l["badge"][0], l["badge"][1], f'Finish "{l["title"]}"'
    for gid, name, em, desc in GLOBAL_BADGES:
        if gid == bid:
            return name, em, desc
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
        ss.err = "Please type a nickname."
        return
    if not ss.get("consent"):
        ss.err = "A parent or guardian needs to be with you. Tick the box when they are."
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
    ss.quiz = build_quiz("lesson", C.LESSON_BY_ID[lid]["bank"], C.QUESTIONS_PER_PLAY, lid)


def build_quiz(kind, pool, n, lid=None):
    qs = []
    for q, opts, ans, why in random.sample(pool, min(n, len(pool))):
        order = list(range(len(opts)))
        random.shuffle(order)
        qs.append(dict(q=q, opts=[opts[j] for j in order], right=order.index(ans), why=why))
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
    ss.quiz = build_quiz("quick", C.band_question_pool(ss.quick_band), C.QUICK_QUIZ_LENGTH)


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
    ss.err = "" if ok else "That is not right. Try again."


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
        for col, b in zip(cols, C.BANDS):
            with col:
                state = "tab-on" if b["id"] == current else "tab"
                with st.container(key=f"{state}-{prefix}-{b['id']}"):
                    st.button(f'{b["name"]}\n{b["ages"].replace("Ages ", "")}', key=f"{prefix}-{b['id']}", on_click=on_pick, args=(b["id"],))


def topbar():
    ss = st.session_state
    with st.container(key="ns-top"):
        c1, c2 = st.columns([2.2, 1.4])
        with c1:
            md('<div class="nk-row"><span style="font-size:1.8rem">🐿️</span><div><div class="nk-title" style="font-size:1.1rem;white-space:nowrap">EasyFin</div><div class="nk-sub" style="margin:0;white-space:nowrap">powered by <b>NYZTrade</b></div></div></div>')
        with c2:
            st.button(THEME_LABEL[ss.theme], key="theme-btn", on_click=cycle_theme)


def nav():
    ss = st.session_state
    items = [("learn", "🎒 Learn"), ("quick", "⚡ Quiz"), ("rewards", "🏆 Rewards"), ("parent", "👪 Parent")]
    with st.container(key="ns-nav"):
        cols = st.columns(len(items))
        for col, (pid, label) in zip(cols, items):
            with col:
                state = "tab-on" if ss.page == pid else "tab"
                with st.container(key=f"{state}-nav-{pid}"):
                    st.button(label, key=f"nav-{pid}", on_click=go, args=(pid,))


def stats_row(P):
    lv, into = level(P["xp"])
    md(f'<div class="nk-stats">'
       f'<div class="nk-stat"><b>⭐ {total_stars(P)}</b><span>stars</span></div>'
       f'<div class="nk-stat"><b>🔥 {P["streak"]}</b><span>day streak</span></div>'
       f'<div class="nk-stat"><b>⚡ {P["xp"]}</b><span>XP</span></div>'
       f'<div class="nk-stat"><b>Lv {lv}</b><span>level</span></div></div>')


def footer():
    md('<div class="nk-foot">Practice money only. EasyFin teaches ideas and habits. It gives no investment advice or tips, '
       'and no real money moves here. Examples use made-up numbers.<br><b>EasyFin</b> · powered by <b>NYZTrade</b></div>')


# ------------------------------------------------------------------ onboarding
def onboarding():
    ss = st.session_state
    md('<div class="nk-hero"><div class="nk-mascot">🐿️</div><div class="nk-title">Hi, I am Chintu!</div>'
       '<small>Welcome to <b>EasyFin</b>. Learn how money works through stories, games and quizzes. Ages 5 to 14.</small><br><small style="opacity:.85">powered by NYZTrade</small></div>')
    names = storage.profile_names()
    if names:
        md('<div class="nk-title" style="font-size:1.05rem">Welcome back</div>')
        for n in names[:8]:
            st.button(f"🐿️ {n}", key=f"prof-{n}", on_click=open_profile, args=(n,))
        md('<div class="nk-sub" style="text-align:center">or start a new learner</div>')
    with st.container(key="card-new"):
        st.text_input("Pick a nickname (not your full name)", key="nick", max_chars=20, placeholder="e.g. Aarav")
        md('<div class="nk-sub">Choose your age group</div>')
        band_buttons(ss.pick_band, pick_onboard_band, "ob")
        st.checkbox("My parent or guardian is with me and agrees", key="consent")
        if ss.err:
            ui.md(f'<div class="nk-fb no">{esc(ss.err)}</div>')
        st.button("Let us start ➜", key="start", type="primary", on_click=start_profile)
    footer()


# ------------------------------------------------------------------ learn
def learn():
    ss = st.session_state
    P = ss.P
    lv, into = level(P["xp"])
    done_n = len(P["done"])
    md(f'<div class="nk-hero"><div class="nk-mascot">🐿️</div><div class="nk-title">Hi {esc(ss.name)}!</div>'
       f'<small>{done_n} of {len(C.LESSONS)} lessons done. Keep going!</small>'
       f'<div style="margin-top:10px;background:rgba(255,255,255,.28);border-radius:99px;height:12px;overflow:hidden"><i style="display:block;height:100%;width:{into}%;background:#FFD27A;border-radius:99px"></i></div>'
       f'<small>Level {lv}, {100 - into} XP to level {lv + 1}</small></div>')
    stats_row(P)
    band_buttons(P["band"], set_band, "lb")
    band = C.BAND_BY_ID[P["band"]]
    md(f'<div class="nk-sub" style="text-align:center">{esc(band["note"])}</div>')
    for l in C.lessons_for(P["band"]):
        s = P["done"].get(l["id"], 0)
        with st.container(key=f"card-{l['id']}"):
            md(f'<div class="nk-row"><div class="nk-art">{l["art"]}</div><div class="nk-grow"><div class="nk-title" style="font-size:1.1rem">{esc(l["title"])}</div>'
               f'<div class="nk-sub">{esc(l["blurb"])}</div></div></div>'
               f'<div class="nk-stars" style="color:var(--sun);margin:6px 0 2px">{ui.stars(s)}</div>')
            st.button("Play again" if s else "Play ➜", key=f"play-{l['id']}", type="secondary" if s else "primary",
                      on_click=open_lesson, args=(l["id"],))


# ------------------------------------------------------------------ lesson
def exit_lesson():
    go("learn")


def lesson_view():
    ss = st.session_state
    l = C.LESSON_BY_ID[ss.lesson]
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
        quiz_view(l["bank"], l)


def story_view(l):
    ss = st.session_state
    n = len(l["story"])
    em, text = l["story"][ss.step]
    md(ui.dots(ss.step, ss.step, n))
    md(f'<div class="nk-story nk-pop"><div class="em">{em}</div><p>{esc(text)}</p></div>')
    if ss.listen:
        ui.listen(text)
    with st.container(key="ns-story-nav"):
        c1, c2 = st.columns([1, 2])
        with c1:
            st.button("◀ Back", key="story-back", on_click=story_move, args=(-1, n), disabled=ss.step == 0)
        with c2:
            st.button("Next ▶" if ss.step < n - 1 else "Let us play! 🎮", key="story-next", type="primary", on_click=story_move, args=(1, n))


def game_view(l):
    ss = st.session_state
    finished = activities.play(l)
    if finished:
        st.button("Take the quiz ➜", key="to-quiz", type="primary", on_click=to_quiz, args=(l["id"],))


def quiz_view(bank, l=None):
    ss = st.session_state
    qz = ss.quiz
    if qz is None:
        to_quiz(l["id"])
        qz = ss.quiz
    if qz["result"]:
        return result_view(l)
    n = len(qz["qs"])
    q = qz["qs"][qz["i"]]
    md(ui.dots(qz["i"], qz["i"], n))
    md(f'<div class="nk-sub" style="text-align:center">Question {qz["i"] + 1} of {n}</div>')
    md(f'<div class="nk-q">{esc(q["q"])}</div>')
    if ss.listen:
        ui.listen(q["q"] + " " + ". ".join(q["opts"]))
    for oi, text in enumerate(q["opts"]):
        if qz["answered"]:
            state = "ok" if oi == q["right"] else "opt"
        else:
            state = "no" if oi in qz["wrong"] else "opt"
        with st.container(key=f"{state}-q{qz['i']}-{oi}"):
            st.button(text, key=f"q{qz['i']}-o{oi}", on_click=pick, args=(oi,), disabled=qz["answered"] or oi in qz["wrong"])
    if qz["answered"]:
        first = not qz["wrong"]
        ui.md(f'<div class="nk-fb ok nk-pop">{"Great job! " if first else "You got it! "}{esc(q["why"])}</div>')
        last = qz["i"] + 1 >= n
        st.button("See my results ➜" if last else "Next question ➜", key="next-q", type="primary", on_click=next_q)
    elif qz["wrong"]:
        ui.md('<div class="nk-fb hint">Not quite. That is okay. Try another answer.</div>')


def result_view(l):
    ss = st.session_state
    qz = ss.quiz
    res = qz["result"]
    n = len(qz["qs"])
    if qz["kind"] == "lesson":
        md(f'<div class="nk-hero nk-pop" style="text-align:center"><div class="nk-title">Lesson complete!</div>'
           f'<div style="font-size:2.6rem;letter-spacing:6px;margin:6px 0">{"⭐" * res["stars"]}{"☆" * (3 - res["stars"])}</div>'
           f'<small>{qz["first_ok"]} of {n} right on the first try. +{qz["xp"]} XP</small></div>')
        md(f'<div class="nk-card"><div class="nk-title" style="font-size:1.05rem">Talk about it at home</div><div class="nk-sub">{esc(l["talk"])}</div></div>')
    else:
        md(f'<div class="nk-hero nk-pop" style="text-align:center"><div class="nk-title">Quick Quiz done!</div>'
           f'<div class="nk-big" style="color:#fff">{qz["first_ok"]} / {n}</div><small>+{qz["xp"]} XP</small></div>')
    for bid in res["new"]:
        name, em, desc = badge_info(bid)
        md(f'<div class="nk-fb hint nk-pop">{em} New badge: <b>{esc(name)}</b>. {esc(desc)}</div>')
    if qz["kind"] == "lesson":
        with st.container(key="ns-res-act"):
            c1, c2 = st.columns(2)
            with c1:
                st.button("Play again", key="res-again", on_click=open_lesson, args=(l["id"],))
            with c2:
                st.button("Back to lessons", key="res-back", type="primary", on_click=go, args=("learn",))
    else:
        with st.container(key="ns-res-act"):
            c1, c2 = st.columns(2)
            with c1:
                st.button("Another round", key="res-again", on_click=start_quick)
            with c2:
                st.button("Back to lessons", key="res-back", type="primary", on_click=go, args=("learn",))


# ------------------------------------------------------------------ quick quiz
def quick_view():
    ss = st.session_state
    P = ss.P
    if ss.quiz and ss.quiz["kind"] == "quick":
        return quiz_view(None, None)
    md('<div class="nk-hero"><div class="nk-mascot">⚡</div><div class="nk-title">Quick Quiz</div>'
       '<small>10 mixed questions from the whole age group. Earn XP and try for 10 out of 10!</small></div>')
    band_buttons(ss.quick_band, pick_quick_band, "qb")
    pool = len(C.band_question_pool(ss.quick_band))
    best = P["quick_best"].get(ss.quick_band)
    md(f'<div class="nk-card"><div class="nk-sub">{pool} questions in this group. Best score: <b>{best if best is not None else "none yet"}</b>{" / 10" if best is not None else ""}</div></div>')
    st.button("Start 10 questions ➜", key="quick-start", type="primary", on_click=start_quick)


# ------------------------------------------------------------------ rewards
def rewards_view():
    ss = st.session_state
    P = ss.P
    lv, into = level(P["xp"])
    md(f'<div class="nk-hero"><div class="nk-mascot">🏆</div><div class="nk-title">Level {lv}</div>'
       f'<small>{P["xp"]} XP in total. {100 - into} XP to the next level.</small>'
       f'<div style="margin-top:10px;background:rgba(255,255,255,.28);border-radius:99px;height:12px;overflow:hidden"><i style="display:block;height:100%;width:{into}%;background:#FFD27A;border-radius:99px"></i></div></div>')
    stats_row(P)
    md('<div class="nk-title" style="margin-top:6px">Lesson badges</div>')
    cells = ""
    for l in C.LESSONS:
        got = "L:" + l["id"] in P["badges"]
        cells += f'<div class="nk-badge {"" if got else "locked"}"><div class="em">{l["badge"][1]}</div><b>{esc(l["badge"][0])}</b><span>{ui.stars(P["done"].get(l["id"], 0))}</span></div>'
    md(f'<div class="nk-grid">{cells}</div>')
    md('<div class="nk-title" style="margin-top:6px">Special badges</div>')
    cells = ""
    for gid, name, em, desc in GLOBAL_BADGES:
        got = gid in P["badges"]
        cells += f'<div class="nk-badge {"" if got else "locked"}"><div class="em">{em}</div><b>{esc(name)}</b><span>{esc(desc)}</span></div>'
    md(f'<div class="nk-grid">{cells}</div>')


# ------------------------------------------------------------------ parent
def parent_view():
    ss = st.session_state
    P = ss.P
    if not ss.parent_ok:
        if "gate_answer" not in ss:
            a, b = random.randint(6, 9), random.randint(6, 9)
            ss.gate_q, ss.gate_answer = f"{a} × {b}", a * b
        md('<div class="nk-hero"><div class="nk-mascot">👪</div><div class="nk-title">Parent corner</div><small>A quick grown-up check, then you can see progress and settings.</small></div>')
        with st.container(key="card-gate"):
            st.text_input(f"What is {ss.gate_q}?", key="gate", max_chars=3)
            if ss.err:
                ui.md(f'<div class="nk-fb no">{esc(ss.err)}</div>')
            st.button("Open", key="gate-open", type="primary", on_click=check_gate)
        return
    acc = round(P["q_first"] / P["q_total"] * 100) if P["q_total"] else 0
    minutes = round(P["seconds"] / 60)
    md(f'<div class="nk-hero"><div class="nk-mascot">👪</div><div class="nk-title">{esc(ss.name)}\'s progress</div>'
       f'<small>Age group: {esc(C.BAND_BY_ID[P["band"]]["name"])} · learning since {esc(P["created"])}</small></div>')
    md(f'<div class="nk-stats"><div class="nk-stat"><b>{len(P["done"])}/{len(C.LESSONS)}</b><span>lessons</span></div>'
       f'<div class="nk-stat"><b>{acc}%</b><span>first-try right</span></div>'
       f'<div class="nk-stat"><b>{minutes}</b><span>minutes</span></div>'
       f'<div class="nk-stat"><b>{P["streak"]}</b><span>day streak</span></div></div>')
    for b in C.BANDS:
        ls = C.lessons_for(b["id"])
        d = sum(1 for l in ls if l["id"] in P["done"])
        md(f'<div class="nk-card"><div class="nk-row"><div class="nk-grow"><div class="nk-title" style="font-size:1rem">{esc(b["name"])} · {esc(b["ages"])}</div>'
           f'<div class="nk-sub">{d} of {len(ls)} lessons</div></div></div><div style="margin-top:6px">{ui.bar(d / len(ls) * 100, True)}</div></div>')
    md('<div class="nk-title" style="margin-top:6px">Talk at home</div>')
    rows = ""
    for l in C.LESSONS:
        s = P["done"].get(l["id"], 0)
        mark = ui.stars(s) if s else "not yet"
        rows += f'<tr><td>{l["art"]} <b>{esc(l["title"])}</b><br><span class="nk-sub">{esc(l["talk"])}</span></td><td style="white-space:nowrap">{mark}</td></tr>'
    md(f'<div class="nk-card"><table class="nk-table"><tr><th>Lesson and conversation starter</th><th>Stars</th></tr>{rows}</table></div>')
    md(f'<div class="nk-card"><div class="nk-title" style="font-size:1rem">Question bank</div><div class="nk-sub">{C.total_questions()} questions across {len(C.LESSONS)} lessons. Each play draws {C.QUESTIONS_PER_PLAY} at random, so replays feel fresh.</div></div>')
    md('<div class="nk-title" style="margin-top:6px">Settings</div>')
    with st.container(key="ns-set"):
        c1, c2 = st.columns(2)
        with c1:
            st.button(THEME_LABEL[ss.theme], key="set-theme", on_click=cycle_theme)
        with c2:
            st.button("🔊 Read aloud: " + ("on" if ss.listen else "off"), key="set-listen", on_click=toggle_listen)
    st.download_button("Download progress (JSON)", storage.export_json(ss.name), file_name=f"easyfin-{ss.name}.json", mime="application/json")
    with st.container(key="ns-set2"):
        c1, c2 = st.columns(2)
        with c1:
            st.button("Switch learner", key="set-switch", on_click=switch_child)
        with c2:
            st.button("🔒 Lock", key="set-lock", on_click=lock_parent)
    if not ss.confirm_reset:
        st.button("Delete this learner's data", key="reset", on_click=ask_reset)
    else:
        ui.md('<div class="nk-fb no">This deletes all progress for this learner. It cannot be undone.</div>')
        with st.container(key="ns-reset"):
            c1, c2 = st.columns(2)
            with c1:
                st.button("Yes, delete", key="reset-yes", on_click=do_reset)
            with c2:
                st.button("Keep it", key="reset-no", on_click=cancel_reset)
    md('<div class="nk-card"><div class="nk-title" style="font-size:1rem">Privacy and safety</div>'
       '<div class="nk-sub">Only a nickname and progress are stored, on this device. No ads, no chat, no real money. '
       'If you run this online for children, get verifiable parental consent as required by the DPDP Act and Rules, and keep the content educational only.</div></div>')


# ------------------------------------------------------------------ main
def main():
    init()
    ss = st.session_state
    ui.inject(ss.theme)
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
