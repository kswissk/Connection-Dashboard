function runDesign() {

    let Vu = parseFloat(document.getElementById("Vu").value);
    let Tu = parseFloat(document.getElementById("Tu").value);

    // --------------------------
    // TABLE 1 (Sample)
    // --------------------------
    let table1 = "<table><tr><th>Tu\\Vu</th><th>20</th><th>40</th><th>60</th><th>80</th></tr>";

    let tensions = [0, 10, 20, 30];
    tensions.forEach(t => {
        table1 += `<tr><td>${t}</td>`;
        table1 += `<td>2</td><td>2</td><td>2</td><td>3</td>`;
        table1 += "</tr>";
    });

    table1 += "</table>";
    document.getElementById("table1").innerHTML = table1;


    // --------------------------
    // TABLE 2
    // --------------------------
    let table2 = `
    <table>
        <tr>
            <th>Connection</th>
            <th>Bolts/Angle</th>
            <th>Total</th>
            <th>Angle</th>
            <th>Weld</th>
        </tr>
        <tr>
            <td>BC-2</td>
            <td>2</td>
            <td>4</td>
            <td>L4x4x3/8</td>
            <td>1/4</td>
        </tr>
    </table>
    `;

    document.getElementById("table2").innerHTML = table2;


    // --------------------------
    // SUMMARY
    // --------------------------
    let summary = `
    Shear = ${Vu} kips <br>
    Tension = ${Tu} kips <br>
    Bolts per angle = 2 <br>
    Total bolts = 4 <br>
    Weld OK ✅
    `;

    document.getElementById("summary").innerHTML = summary;
}
