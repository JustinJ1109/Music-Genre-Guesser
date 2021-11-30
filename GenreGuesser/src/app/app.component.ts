import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { RestService } from './rest.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{

  title = 'GenreGuesser';
  files: File[] = [];
  testOutput = 'test'
  url = 'http://127.0.0.1'

  spectrogramImage: JSON;
  predictions: JSON;
  employeeData: JSON;

  constructor(private rs : RestService) {}

  headers = ["day","temperature", "windspeed",  "event"]
  weather: Array<string>;

  ngOnInit() {
    this.rs.readWeather()
      .subscribe
        (
          (response:any) => 
          {
            this.weather = response[0]["data"];
            console.log(response)
            
          },
          (error:any) =>
          {
            console.log("No Data Found " + JSON.stringify(error));
          }
        )
  }

  onSelect(event: any) {
    console.log(event);
    this.files.push(...event.addedFiles);
  }
  
  onRemove(event: any) {
    console.log(event);
    this.files.splice(this.files.indexOf(event), 1);
  }




  onButtonClick() {

    this.rs.sendImage(this.files[0]);

    let audio = new Audio();
    audio.src = "../../../assets/StarWars3.wav";
    audio.load();
    audio.play();
    

    
    

    //send chosen file to backend, recieve ArrayList of top 5 genres with percentages
    //also recieve image of spectrogram, load into box
    //this.testOutput = "test updated"

    //this.http.get('http://127.0.0.1:5002/spectrogram').subscribe(data => {
    //  this.spectrogramImage = data as JSON;
    //  console.log("image test " + this.spectrogramImage);
    //})

    //this.http.get('http://127.0.0.1:5002/predictions').subscribe(data => {
    //  this.predictions = data as JSON;
    //  console.log(this.predictions);
    //})
  }
}

