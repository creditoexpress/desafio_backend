import {
  Entity,
  ObjectIdColumn,
  Column,
  CreateDateColumn,
  UpdateDateColumn,
} from 'typeorm';

@Entity('rates')
export class Rate {
  @ObjectIdColumn()
  id: string;

  @Column()
  type: string;

  @Column()
  installments: number;

  @Column()
  rate: number;

  @CreateDateColumn()
  created_at?: Date;

  @UpdateDateColumn()
  updated_at?: Date;
}
