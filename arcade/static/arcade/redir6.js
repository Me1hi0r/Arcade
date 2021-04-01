let quests = ['faces', 'harp', 'triangle', 'tags', 'bowman', 'color_memory', 'cube', 'tubes', 'castle', 'holes', 'memory', 'maze', 'tower']
// let count = 0;
let count = localStorage.getItem('count');

// let quest = quests[count]; 
// setTimeout('location.replace(`http://127.0.0.1:8000/leaderboard/${quests[count]}/`)', 5000);
setTimeout('location.replace(`http://127.0.0.100:8001/leaderboard/${quests[count]}/`)', 5000);
count++;
if (count == quests.length - 1) {
  localStorage.setItem('count', 0);
} else {
  localStorage.setItem('count', count);
}