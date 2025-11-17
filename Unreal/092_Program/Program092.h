// Multiplayer
// Program 092

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program092.generated.h"

UCLASS()
class AProgram092 : public AActor
{
    GENERATED_BODY()

public:
    AProgram092();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
