import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http:HttpClient, private router:Router) { }

  httpOptions = {
    headers: new HttpHeaders(
      {
        'Content-Type': 'application/json',
        'Accept':'application/json'
      }
    )
  }

  
  register(data:any){
    
    this.http.post("http://127.0.0.1:8000/api/employee/register/",JSON.stringify(data),this.httpOptions).subscribe(
      ()=>{
        console.log("Registered")
        this.router.navigate(['/login'])
      },
      error => {
        console.log(error)
      }
    )
  }

  login(data:any):Observable<any>{
    return this.http.post("http://127.0.0.1:8000/api/employee/login/",JSON.stringify(data),this.httpOptions)
  }

}
