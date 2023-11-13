```
 local GameId = "PUT PLACE ID HERE FOR SCRIPT TO WORK" 

function Touched(Player)
    local FromChar = game.Players:GetPlayerFromCharacter(Player.Parent)
    if FromChar then
        local TeleService = game:GetService("TeleportService")
        TeleService:Teleport(GameId,FromChar)
    end
end
script.Parent.Touched:Connect(Touched) 
```