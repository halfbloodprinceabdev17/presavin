document.getElementById('stock-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    try {
        const response = await fetch('/search', {
            method: 'POST',
            body: formData,
        });
        const data = await response.json();

        if (response.ok) {
            document.getElementById('stock-title').textContent =
                `Stock: ${data.stock_info.name} (${data.stock_info.symbol})`;
            document.getElementById('stock-price').textContent =
                `Current Price: ₹${data.stock_info.current_price}`;
            document.getElementById('growth-1y').textContent = data.stock_info.growth_rates["1_year"];
   
            document.getElementById('growth-5y').textContent = data.stock_info.growth_rates["5_year"];
            
        } else {
            alert(data.error);
        }
    } catch (error) {
        alert("An error occurred: " + error.message);
    }
});
