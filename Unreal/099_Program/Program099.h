// Game Instance Subsystem
// Program 099

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program099.generated.h"

UCLASS()
class AProgram099 : public AActor
{
    GENERATED_BODY()

public:
    AProgram099();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
