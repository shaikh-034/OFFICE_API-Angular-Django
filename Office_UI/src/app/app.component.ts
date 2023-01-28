import { Component } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Office_UI';
  constructor(private cookie:CookieService){

  }

  logout(){
    this.cookie.deleteAll()
  }

  isAuthenticated(){
    if(this.cookie.get('user')){
      return false
    }
    return true
  }
}
