  // Set the sale end time (3 days from the current time)
  const saleEndTime = new Date();
  saleEndTime.setDate(saleEndTime.getDate() + 27);
  
  // Function to update the countdown timer
  function updateCountdown() {
      const now = new Date();
      const timeDifference = saleEndTime - now;
  
      if (timeDifference <= 0) {
          document.getElementById("timer").innerHTML = "<p>Sale has ended!</p>";
          return;
      }
  
      const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
      const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);
  
      document.getElementById("days").innerText = days.toString().padStart(2, '0');
      document.getElementById("hours").innerText = hours.toString().padStart(2, '0');
      document.getElementById("minutes").innerText = minutes.toString().padStart(2, '0');
      document.getElementById("seconds").innerText = seconds.toString().padStart(2, '0');
  }
  
  // Update the countdown every second
  setInterval(updateCountdown, 1000);
  
  // Initial call to set the timer immediately
  updateCountdown();
  