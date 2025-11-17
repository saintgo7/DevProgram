// Spring Arm
// Program 083

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program083.generated.h"

UCLASS()
class AProgram083 : public AActor
{
    GENERATED_BODY()

public:
    AProgram083();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
