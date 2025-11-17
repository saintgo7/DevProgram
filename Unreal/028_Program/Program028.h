// Loop Timer
// Program 028

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program028.generated.h"

UCLASS()
class AProgram028 : public AActor
{
    GENERATED_BODY()

public:
    AProgram028();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
