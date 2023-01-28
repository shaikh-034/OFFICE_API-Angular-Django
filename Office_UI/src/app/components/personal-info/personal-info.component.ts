import { Component, OnInit } from '@angular/core';
import { PersonalInfoService } from 'src/app/services/personal-info.service';
import { CookieService } from 'ngx-cookie-service';
import jwtDecode from 'jwt-decode';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-personal-info',
  templateUrl: './personal-info.component.html',
  styleUrls: ['./personal-info.component.css'],
})
export class PersonalInfoComponent implements OnInit {

  constructor(private infoservice:PersonalInfoService,private cookie:CookieService,private datePipe:DatePipe) { }

  ngOnInit(): void {
  }
personalInfo(data:any){
  let token:any = jwtDecode(this.cookie.get('user'))
  data.value.user=(token.user_id)
  data.value.DOB= this.datePipe.transform( data.value.DOB,'yyyy-MM-dd')
  console.log(data.value)
  this.infoservice.personalInfo(data.value)
}

}
