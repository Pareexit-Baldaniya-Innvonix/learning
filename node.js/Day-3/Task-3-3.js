// Task 3:
// 3. Method overloading:

function Add(datatype, ...args) {
    let answer;

    if(datatype == 'int') {
        answer = 0;
    }

    if(datatype == 'str') {
        answer = "";
    }

    for (let x = 0; x < args.length; x++) {
        answer += args[x];
    }
    console.log(answer);
}

Add('int', 5, 5)
Add('str', "Hello ", "World");