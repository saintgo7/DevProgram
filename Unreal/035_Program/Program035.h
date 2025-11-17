// Animation Notify
// Program 035

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program035.generated.h"

UCLASS()
class AProgram035 : public AActor
{
    GENERATED_BODY()

public:
    AProgram035();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
