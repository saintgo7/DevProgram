// Main Menu
// Program 050

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program050.generated.h"

UCLASS()
class AProgram050 : public AActor
{
    GENERATED_BODY()

public:
    AProgram050();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
