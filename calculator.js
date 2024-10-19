let data = [];

// Step 1: Dapatkan jumlah data yang akan diinput
function getDataCount() {
    const dataCount = document.getElementById('dataCount').value;
    if (dataCount > 0) {
        document.getElementById('input-section').style.display = 'none';
        generateNumberInputs(dataCount);
    } else {
        alert('Masukkan jumlah data yang valid.');
    }
}

// Step 2: Generate input fields sesuai jumlah data
function generateNumberInputs(count) {
    const numberInputs = document.getElementById('numberInputs');
    numberInputs.innerHTML = ''; // Bersihkan input sebelumnya
    for (let i = 0; i < count; i++) {
        const input = document.createElement('input');
        input.type = 'number';
        input.className = 'number-input';
        input.placeholder = `Masukkan angka ke-${i + 1}`;
        numberInputs.appendChild(input);
    }
    document.getElementById('data-input-section').style.display = 'block';
}

// Step 3: Submit data yang diinput dan tampilkan di header
function submitNumbers() {
    const inputs = document.getElementsByClassName('number-input');
    data = [];
    for (let input of inputs) {
        const value = parseFloat(input.value);
        if (!isNaN(value)) {
            data.push(value);
        }
    }
    if (data.length > 0) {
        data.sort((a, b) => a - b); // Sort data
        document.getElementById('dataDisplay').innerText = `Data: ${data.join(', ')}`;
        document.getElementById('data-header').style.display = 'block';
        document.getElementById('analysis-menu').style.display = 'block';
        document.getElementById('data-input-section').style.display = 'none';
    } else {
        alert('Masukkan semua angka dengan benar.');
    }
}

// Step 4: Analisis statistika
function calculateMean() {
    const sum = data.reduce((a, b) => a + b, 0);
    const mean = sum / data.length;
    const formula = `Rumus Mean: (${data.join(' + ')}) / ${data.length}`;
    displayResult(`${formula} = ${mean}\nRata-rata (Mean): ${mean}`);
}

function calculateMode() {
    const frequency = {};
    data.forEach(num => frequency[num] = (frequency[num] || 0) + 1);
    const maxFrequency = Math.max(...Object.values(frequency));
    const modes = Object.keys(frequency).filter(num => frequency[num] === maxFrequency);
    const formula = `Modus adalah nilai yang paling sering muncul.`;
    displayResult(`${formula}\nModus: ${modes.length > 1 ? modes.join(', ') : modes[0]}`);
}

function calculateMedian() {
    const middle = Math.floor(data.length / 2);
    let median;
    if (data.length % 2 === 0) {
        median = (data[middle - 1] + data[middle]) / 2;
        const formula = `Rumus Median: (data[${middle - 1}] + data[${middle}]) / 2`;
        displayResult(`${formula} = ${(data[middle - 1] + data[middle]) / 2}\nMedian: ${median}`);
    } else {
        median = data[middle];
        const formula = `Median adalah nilai tengah dari data terurut.\nMedian: data[${middle}] = ${data[middle]}`;
        displayResult(`${formula}\nMedian: ${median}`);
    }
    return median;
}

function calculateMidrange() {
    const midrange = (data[0] + data[data.length - 1]) / 2;
    const formula = `Rumus Midrange: (nilai minimum + nilai maksimum) / 2`;
    displayResult(`${formula} = (${data[0]} + ${data[data.length - 1]}) / 2 = ${midrange}\nMidrange: ${midrange}`);
}

function calculateMidhinge() {
    const Q1 = data[Math.floor(data.length / 4)];
    const Q3 = data[Math.floor(data.length * 3 / 4)];
    const midhinge = (Q1 + Q3) / 2;
    const formula = `Rumus Midhinge: (Q1 + Q3) / 2`;
    displayResult(`${formula} = (${Q1} + ${Q3}) / 2 = ${midhinge}\nMidhinge: ${midhinge}`);
}

// Step 5: Hitung Kuartil dengan interpolasi
function calculateQuartiles() {
    const n = data.length;

    function interpolateQuartile(pos) {
        const lower = Math.floor(pos);
        const upper = Math.ceil(pos);
        if (lower === upper) {
            return data[lower - 1];
        } else {
            return data[lower - 1] + (pos - lower) * (data[upper - 1] - data[lower - 1]);
        }
    }

    const Q1_pos = 0.25 * (n + 1);
    const Q2_pos = 0.50 * (n + 1);
    const Q3_pos = 0.75 * (n + 1);

    const Q1 = interpolateQuartile(Q1_pos);
    const Q2 = interpolateQuartile(Q2_pos);
    const Q3 = interpolateQuartile(Q3_pos);

    const formula = `Kuartil dihitung dengan interpolasi pada posisi:\nQ1 = Posisi 0.25*(n+1) = ${Q1_pos}\nQ2 = Posisi 0.50*(n+1) = ${Q2_pos}\nQ3 = Posisi 0.75*(n+1) = ${Q3_pos}`;
    displayResult(`${formula}\nKuartil 1 (Q1): ${Q1}, Kuartil 2 (Median/Q2): ${Q2}, Kuartil 3 (Q3): ${Q3}`);
    return { Q1, Q2, Q3 };
}

// Step 6: Hitung IQR
function calculateIQR() {
    const { Q1, Q3 } = calculateQuartiles();
    const IQR = Q3 - Q1;
    const formula = `Rumus IQR: Q3 - Q1 = ${Q3} - ${Q1}`;
    displayResult(`${formula} = ${IQR}\nJangkauan Antar Kuartil (IQR): ${IQR}`);
    return IQR;
}

// Function untuk menampilkan hasil analisis
function displayResult(result) {
    const resultSection = document.getElementById('result');
    resultSection.innerHTML = `<pre>${result}</pre>`;
}

// Fungsi untuk menampilkan diagram Stem-and-Leaf
function stemAndLeaf() {
    const stems = {};
    data.forEach(num => {
        const stem = Math.floor(num / 10);
        const leaf = num % 10;
        if (!stems[stem]) {
            stems[stem] = [];
        }
        stems[stem].push(leaf);
    });

    let result = "Stem | Leaf\n------------\n";
    for (const [stem, leaves] of Object.entries(stems)) {
        result += `${stem}    | ${leaves.sort((a, b) => a - b).join(" ")}\n`;
    }

    displayResult(result);
}

// Fungsi untuk menampilkan Box-Whisker Plot
function boxWhiskerPlot() {
    const { Q1, Q2, Q3 } = calculateQuartiles();
    const IQR = Q3 - Q1;

    const LIF = Q1 - 1.5 * IQR; // Lower Inner Fence
    const UIF = Q3 + 1.5 * IQR; // Upper Inner Fence
    const LOF = Q1 - 3.0 * IQR; // Lower Outer Fence
    const UOF = Q3 + 3.0 * IQR; // Upper Outer Fence

    const outliers = data.filter(num => num < LIF || num > UIF); // Pencilan
    const minData = data.filter(num => num >= LIF)[0];
    const maxData = data.filter(num => num <= UIF).slice(-1)[0];

    const boxPlot = `
        Box-Whisker Plot:
        --------------------------------------
        Lower Outer Fence (LOF): ${LOF}
        Lower Inner Fence (LIF): ${LIF}
        Q1 (Lower Quartile): ${Q1}
        Median (Q2): ${Q2}
        Q3 (Upper Quartile): ${Q3}
        Upper Inner Fence (UIF): ${UIF}
        Upper Outer Fence (UOF): ${UOF}
        --------------------------------------
        Min (Non-Outlier): ${minData}
        Max (Non-Outlier): ${maxData}
        Outliers: ${outliers.length > 0 ? outliers.join(', ') : 'Tidak ada'}
    `;

    displayResult(boxPlot);
}
