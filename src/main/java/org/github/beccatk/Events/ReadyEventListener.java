package org.github.beccatk.Events;

import net.dv8tion.jda.api.events.ReadyEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

public class ReadyEventListener extends ListenerAdapter {
    @Override
    public void onReady(ReadyEvent event){
        System.out.println("TEST");
    }
}
