import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers:[AuthService]
})
export class LoginComponent implements OnInit {

  constructor(private auth:AuthService,private router: Router, private cookie:CookieService) { }

  ngOnInit(): void {
  }

  login(data:NgForm){
    console.log("data",data.value)
    this.auth.login(data.value).subscribe(
      (res:any)=>{
        console.log("Logged In")
        console.log(res.token.access)
        this.cookie.set('user',res.token.access)
        this.router.navigate(['/personalInfo'])
      },
      error => {
        console.log(error)
      }
    )
  }

}
