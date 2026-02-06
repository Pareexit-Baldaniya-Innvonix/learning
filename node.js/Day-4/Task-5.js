// Task 5:
function timer(func) {
    return async function(...args) {
        const startTime = process.hrtime.bigint(); // start time
        const result = await func(...args); // Run the original function
        const endTime = process.hrtime.bigint(); // end time

        const seconds = Number(endTime - startTime) / 1_000_000_000;
        console.log(`Time taken: ${seconds.toFixed(4)} seconds.`);
    };
}

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function wasteTime() {
    await sleep(1000); // Wait for 1 second
    console.log("Function finished!");
}

const timedWasteTime = timer(wasteTime);

timedWasteTime();