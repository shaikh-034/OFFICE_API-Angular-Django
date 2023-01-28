import { Component, OnInit } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { PersonalInfoService } from 'src/app/services/personal-info.service';
import jwtDecode from 'jwt-decode';
import { DatePipe } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {

  constructor(private emp:PersonalInfoService,private cookie:CookieService,private datepipe:DatePipe,private router:Router) { }

  profile:any
  profileInfo:any
  payload:any

  ngOnInit(): void {
    let token = this.cookie.get('user')
    this.payload = jwtDecode(token)
    this.profile=this.emp.employee(this.payload.user_id).subscribe(
      (res)=>{
        this.profileInfo=res
        this.profileInfo.profile.DOB=this.datepipe.transform(this.profileInfo.profile.DOB,'yyyy-MM-dd')
        console.log(this.profileInfo)
        return res
      },
      error=>{
        console.log(error)
      }
    )

  }
  update(data:any){
    data.value.user=this.payload.user_id
    data.value.DOB= this.datepipe.transform( data.value.DOB,'yyyy-MM-dd')
    console.log("Updated",data.value)
    this.emp.employee_update(data.value).subscribe(
      (res)=>{
        console.log(res)
      },
      error=>{
        console.log(error)
      }
    )
  }

  delete(){
    this.emp.employee_delete(this.profileInfo.profile.personal_id).subscribe(
      (res)=>{
        console.log(res)
        this.router.navigate(['/personalInfo'])
      },
      error=>{
        console.log(error)
      }
    )
  }

}
