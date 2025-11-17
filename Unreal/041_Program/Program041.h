// Damage System
// Program 041

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program041.generated.h"

UCLASS()
class AProgram041 : public AActor
{
    GENERATED_BODY()

public:
    AProgram041();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
