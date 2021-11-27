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
  }
}

