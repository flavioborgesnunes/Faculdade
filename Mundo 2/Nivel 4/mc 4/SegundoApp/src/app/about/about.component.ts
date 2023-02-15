import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent {
  num: string | null = "";

 constructor(private route: ActivatedRoute) { }

 ngOnInit(): void {
 this.route.paramMap.subscribe(params => {
 this.num = params.get("id");
 });
 }
}
