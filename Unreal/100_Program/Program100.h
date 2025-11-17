// Local Player Subsystem
// Program 100

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program100.generated.h"

UCLASS()
class AProgram100 : public AActor
{
    GENERATED_BODY()

public:
    AProgram100();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
