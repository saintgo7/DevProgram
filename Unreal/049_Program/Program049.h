// HUD
// Program 049

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program049.generated.h"

UCLASS()
class AProgram049 : public AActor
{
    GENERATED_BODY()

public:
    AProgram049();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
