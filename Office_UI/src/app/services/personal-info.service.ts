import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class PersonalInfoService {

  constructor(private http:HttpClient, private router:Router) { }

  httpOptions = {
    headers: new HttpHeaders(
      {
        'Content-Type': 'application/json',
        'Accept':'application/json',
      }
    )
  }

  id?:Number
  
  personalInfo(data:any){
    this.id=data.user
    this.http.post("http://127.0.0.1:8000/api/employee/info/",JSON.stringify(data),this.httpOptions).subscribe(
      ()=>{
        console.log("Inserted")
        this.router.navigate(['/personalInfo'])
      },
      error => {
        console.log(error)
      }
    )
  }

  employee(id:Number){
    this.id=id
    return this.http.get(`http://127.0.0.1:8000/api/employee/info/${id}`)
  }

  employee_update(data:any){
    return this.http.put(`http://127.0.0.1:8000/api/employee/info/${this.id}`,JSON.stringify(data),this.httpOptions)
  }

  employee_delete(id:Number){
    console.log(id)
    return this.http.delete(`http://127.0.0.1:8000/api/employee/info/${id}`)
  }
}
