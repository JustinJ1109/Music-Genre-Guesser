import { Injectable, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RestService implements OnInit{

  


  constructor(private http : HttpClient) { }

  ngOnInit() {
  }

  url : string = "http://127.0.0.1:5000/";

  readWeather() {
    return this.http.get(this.url, {responseType: 'text'});
  }

  sendImage(file: File): Observable<any> {
    const formData = new FormData();
    formData.append('myFile', file);
    return this.http.post(this.url, formData);
  }

}


