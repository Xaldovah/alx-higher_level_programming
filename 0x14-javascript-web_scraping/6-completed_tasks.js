#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.log(error);
    process.exit(1);
  }

  const tasks = JSON.parse(body);
  const completedTasks = {};

  for (const task of tasks) {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  }

  console.log(completedTasks);
});
