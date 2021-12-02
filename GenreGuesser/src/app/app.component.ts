import { Component, OnInit } from '@angular/core';
import { RestService } from './rest.service';
import { HttpClient } from '@angular/common/http';

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

  responseString: String;

  prediction1: String;
  prediction2: String;
  prediction3: String;
  
  percentage1: String;
  percentage2: String;
  percentage3: String;

  submitted: boolean = false


  constructor(private rs : RestService) {}

  headers = ["genre","percentage"]
  weather: Array<string>;

  ngOnInit() {
    this.rs.readData()
      .subscribe
        (
          (response:any) => 
          {
            console.log(JSON.stringify(response));
            this.responseString = JSON.stringify(response);

            this.responseString = this.responseString.replace(/,/g, "")
            this.responseString = this.responseString.replace(/{/g, "")
            this.responseString = this.responseString.replace(/}/g, "")
            this.responseString = this.responseString.replace(/\[/g, "")
            this.responseString = this.responseString.replace(/\//g, "")
            this.responseString = this.responseString.replace(/\\/g, "")
            this.responseString = this.responseString.replace(/]/g, "")
            this.responseString = this.responseString.replace(/"/g, "")
            this.responseString = this.responseString.replace(/ n /g, "")
            this.responseString = this.responseString.replace(/n /g, "")
            this.responseString = this.responseString.replace(/nn/g, "")
            this.responseString = this.responseString.replace(/data:/g, "")
            this.responseString = this.responseString.replace(/       /g, " ")
            this.responseString = this.responseString.replace(/     /g, " ")
            this.responseString = this.responseString.replace(/    /g, " ")

            console.log(this.responseString);

            this.prediction1 = this.responseString.substring(this.responseString.indexOf("genre1: "), this.responseString.indexOf(" percentage1"))
            this.prediction1 = this.prediction1.substring(8)
            console.log(this.prediction1)

            this.percentage1 = this.responseString.substring(this.responseString.indexOf("percentage1: "), this.responseString.indexOf(" genre2"))
            this.percentage1 = this.percentage1.substring(13)
            console.log(this.percentage1)

            this.prediction2 = this.responseString.substring(this.responseString.indexOf("genre2: "), this.responseString.indexOf(" percentage2"))
            this.prediction2 = this.prediction2.substring(8)
            console.log(this.prediction2)

            this.percentage2 = this.responseString.substring(this.responseString.indexOf("percentage2: "), this.responseString.indexOf(" genre3"))
            this.percentage2 = this.percentage2.substring(13)
            console.log(this.percentage2)

            this.prediction3 = this.responseString.substring(this.responseString.indexOf("genre3: "), this.responseString.indexOf(" percentage3"))
            this.prediction3 = this.prediction3.substring(8)
            console.log(this.prediction3)

            this.percentage3 = this.responseString.substring(this.responseString.indexOf("percentage3: "), this.responseString.length - 1)
            this.percentage3 = this.percentage3.substring(13)
            console.log(this.percentage3)

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

  onSubmit() {
    this.submitted = true;
 }
}

