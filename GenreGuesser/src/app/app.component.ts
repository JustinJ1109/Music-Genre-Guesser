import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  title = 'GenreGuesser';
  files: File[] = [];
  testOutput = 'test'

  prediction1: JSON
  prediction2: JSON
  prediction3: JSON
  prediction4: JSON
  prediction5: JSON
  prediction6: JSON
  prediction7: JSON
  prediction8: JSON
  prediction9: JSON
  prediction10: JSON
  spectrogramImage: JSON;
  predictions: JSON;

  constructor(private http: HttpClient) {}

  onSelect(event: any) {
    console.log(event);
    this.files.push(...event.addedFiles);
  }
  
  onRemove(event: any) {
    console.log(event);
    this.files.splice(this.files.indexOf(event), 1);
  }

  onButtonClick() {
    //send chosen file to backend, recieve ArrayList of top 5 genres with percentages
    //also recieve image of spectrogram, load into box
    this.testOutput = "test updated"

    this.http.get('http://127.0.0.1:5002/spectrogram').subscribe(data => {
      this.spectrogramImage = data as JSON;
      console.log("image test " + this.spectrogramImage);
    })

    this.http.get('http://127.0.0.1:5002/predictions').subscribe(data => {
      this.predictions = data as JSON;
      console.log(this.predictions);
    })

    this.http.get('http://127.0.0.1:5002/prediction1').subscribe(data => {
      this.prediction1 = data as JSON;
      console.log(this.prediction1);
    })
    this.http.get('http://127.0.0.1:5002/prediction2').subscribe(data => {
      this.prediction2 = data as JSON;
      console.log(this.prediction2);
    })
    this.http.get('http://127.0.0.1:5002/prediction3').subscribe(data => {
      this.prediction3 = data as JSON;
      console.log(this.prediction3);
    })
    this.http.get('http://127.0.0.1:5002/prediction4').subscribe(data => {
      this.prediction4 = data as JSON;
      console.log(this.prediction4);
    })
    this.http.get('http://127.0.0.1:5002/prediction5').subscribe(data => {
      this.prediction5 = data as JSON;
      console.log(this.prediction5);
    })
    this.http.get('http://127.0.0.1:5002/prediction6').subscribe(data => {
      this.prediction6 = data as JSON;
      console.log(this.prediction6);
    })
    this.http.get('http://127.0.0.1:5002/prediction7').subscribe(data => {
      this.prediction7 = data as JSON;
      console.log(this.prediction7);
    })
    this.http.get('http://127.0.0.1:5002/prediction8').subscribe(data => {
      this.prediction8 = data as JSON;
      console.log(this.prediction8);
    })
    this.http.get('http://127.0.0.1:5002/prediction9').subscribe(data => {
      this.prediction9 = data as JSON;
      console.log(this.prediction9);
    })
    this.http.get('http://127.0.0.1:5002/prediction10').subscribe(data => {
      this.prediction10 = data as JSON;
      console.log(this.prediction10);
    })
  }
}

