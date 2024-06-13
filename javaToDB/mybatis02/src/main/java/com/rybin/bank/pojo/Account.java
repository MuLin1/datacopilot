package com.rybin.bank.pojo;

import java.util.Arrays;

public class Account {
    private long id;
    private String actno;
    private long balance;

    public Account() {}

    public Account(long id, String actno, long balance) {
        this.id = id;
        this.actno = actno;
        this.balance = balance;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getActno() {
        return actno;
    }

    public void setActno(String actno) {
        this.actno = actno;
    }

    public long getBalance() {
        return balance;
    }

    public void setBalance(long balance) {
        this.balance = balance;
    }

    @Override
    public String toString() {
        return "Account{" +
                "id=" + id +
                ", actno='" + actno + '\'' +
                ", balance=" + balance +
                '}';
    }
}
