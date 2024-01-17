import { Component } from '@angular/core';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent {

  constructor(
  ){}

  navigationList = [{
    name:'hotel', link:'/hotel',icon:'hotel'
  },{
    name: 'customer', link: '/customer',icon:'people'
  },
  {
    name: 'branch', link: '/branch',icon:'house'
  }
  ,{
    name: 'invoice', link: '/invoice',icon:'receipt'
  }
]
}
